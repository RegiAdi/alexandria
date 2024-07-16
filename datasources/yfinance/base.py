import sys
import yfinance as yf


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
export_to_csv_income_statement(ticker)
export_to_csv_balance_sheet(ticker)

income_statement = get_income_statement(ticker)
print(income_statement.index)
print(income_statement.columns)
print(income_statement.T)
