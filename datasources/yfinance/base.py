import sys
import yfinance as yf
from re import sub
from pymongo import MongoClient


def get_database(dbname):

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[dbname]


def get_ticker(ticker_symbol):
    return yf.Ticker(ticker_symbol)


def get_balance_sheet(ticker):
    return ticker.balance_sheet


def get_quarterly_balance_sheet(ticker):
    return ticker.quarterly_balance_sheet


def get_balance_sheet(ticker):
    return ticker.balance_sheet


def get_income_statement(ticker):
    return ticker.income_stmt


def export_to_csv_balance_sheet(ticker):
    ticker_balance_sheet = get_balance_sheet(ticker)
    ticker_balance_sheet.to_csv(ticker.ticker + "_balance_sheet.csv")


def export_to_csv_quarterly_balance_sheet(ticker):
    ticker_quarterly_balance_sheet = get_quarterly_balance_sheet(ticker)
    ticker_quarterly_balance_sheet.to_csv(
        ticker.ticker + "_quarterly_balance_sheet.csv"
    )


def export_to_csv_income_statement(ticker):
    ticker_income_statement = get_income_statement(ticker)
    ticker_income_statement.to_csv(ticker.ticker + "_income_statement.csv")


def to_snake_case(s):
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


ticker_symbol = sys.argv[1]

print(ticker_symbol)

ticker = get_ticker(ticker_symbol)
# export_to_csv_income_statement(ticker)
# export_to_csv_balance_sheet(ticker)

income_statement = get_income_statement(ticker)
# print(income_statement.index)
# print(income_statement.columns)
# print(income_statement.T)

db = get_database("alexandria_db")
income_statement_collection = db["income_statement"]
price_history_collection = db["price_history"]
income_statements = []

for label, content in income_statement.items():
    content_dict = content.to_dict()
    new_content_dict = {}

    for key, value in content_dict.items():
        # print(f"{to_snake_case(key)} - {value}")
        new_content_dict[to_snake_case(key)] = value

    income_stmt = {
        "symbol": ticker_symbol,
        "timestamp": label,
        "data": new_content_dict,
    }

    result = income_statement_collection.replace_one(
        {"symbol": ticker_symbol, "timestamp": label}, income_stmt, upsert=True
    )
    # print(result)

# share_count = ticker.get_shares_full(start="2024-01-01", end=None)

history = ticker.history(interval="1d", period="1y")

# insert price history to db
for row in history.itertuples():
    print(row)

    price_history = {
        "symbol": ticker_symbol,
        "interval": "1d",
        "timestamp": row[0].isoformat(),
        "open": row[1],
        "high": row[2],
        "low": row[3],
        "close": row[4],
        "volume": row[5],
    }

    result = price_history_collection.replace_one(
        {"symbol": ticker_symbol, "timestamp": row[0].isoformat()},
        price_history,
        upsert=True,
    )

# results = price_history_collection.find_one({"timestamp": "2024-10-15T00:00:00+07:00"})

# print(results)

# for document in results:
#     print(document)
# print(document["timestamp"])

# content_dict = content.to_dict()
# new_content_dict = {}

# print(label)
# print(content_dict)

# df_json = income_statement.to_json("BMRI.json")
# df_dict = income_statement.to_dict()

# json.dumps(df_json)
# print(df_dict)
# print(share_count)
# print(history)

# income_statement_data = {"income_statement": df_json}
