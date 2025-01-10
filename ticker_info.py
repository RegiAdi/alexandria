import sqlite3
import time
import json
from ulid import ULID

def get_info(ticker):
    try:
        db = sqlite3.connect("database/alexandria.db")
        print("Opened database successfully")
        cursor = db.cursor()

        yfinance_ticker_info = ticker.info 
        
        new_ulid = ULID()
        time.sleep(0.001)

        cursor.execute("""
            SELECT symbol
            FROM ticker_info
            WHERE symbol = ?""",
            (ticker.ticker,)
        )

        rows = cursor.fetchone()
        print('rows', rows)

        if rows is None:
            cursor.execute("""
                INSERT INTO ticker_info 
                (id, symbol, data) 
                VALUES (?, ?, ?)""", 
                (bytes(new_ulid), ticker.ticker, json.dumps(yfinance_ticker_info))
            )
        else:
            print("Ticker info exist.")

        db.commit()
        db.close()
        print("Closed database successfully")
    except sqlite3.Error as e:
        print(f"Error selecting data: {e}")

