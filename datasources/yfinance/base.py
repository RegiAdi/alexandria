import sys
import yfinance as yf


def get_ticker_data(ticker):
    return yf.Ticker(ticker)


def get_quarterly_balance_sheet(ticker_data):
    return ticker_data.quarterly_balance_sheet


# hist = stock.history(period="5d", interval="1m")
# print(stock.income_stmt)
# print(stock.balance_sheet)

print(sys.argv[1] + ".JK")

ticker = get_ticker_data(sys.argv[1] + ".JK")
ticker_quarterly_balance_sheet = get_quarterly_balance_sheet(ticker)

ticker_quarterly_balance_sheet.to_csv(sys.argv[1] + "_quarterly_balance_sheet.csv")
