import sys
import yfinance as yf
from pymongo import MongoClient


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["alexandria"]


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


ticker_symbol = sys.argv[1] + ".JK"

print(ticker_symbol)

ticker = get_ticker(ticker_symbol)
# export_to_csv_income_statement(ticker)
# export_to_csv_balance_sheet(ticker)

income_statement = get_income_statement(ticker)
print(income_statement.index)
print(income_statement.columns)
print(income_statement.T)

share_count = ticker.get_shares_full(start="2024-01-01", end=None)

df_json = income_statement.to_json()
# df_dict = income_statement.to_dict()

print(df_json)
# print(df_dict)
# print(share_count)

income_statement_data = {"income_statement": df_json}

db = get_database()
income_statement_collection = db["income_statement"]
income_statement_collection.insert_one(income_statement_data)
