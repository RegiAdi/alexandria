import sqlite3
import time
from ulid import ULID

def get_dividends(ticker):
    try:
        db = sqlite3.connect("database/alexandria.db")
        print("Opened database successfully")
        cursor = db.cursor()

        yfinance_dividends = ticker.get_dividends()
        
        dividends = [] 

        for key, value in yfinance_dividends.items():
            new_ulid = ULID()
            time.sleep(0.001)

            cursor.execute("""
                SELECT symbol, amount, timestamp
                FROM dividends
                WHERE symbol = ?
                AND timestamp = ?""",
                (ticker.ticker, key.to_pydatetime())
            )

            rows = cursor.fetchone()
            print(rows)

            if rows is None:
                dividends.append((
                    bytes(new_ulid), 
                    ticker.ticker, 
                    value, 
                    key.to_pydatetime()
                ))
            else:
                print("Dividend exist.")

        cursor.executemany("""
            INSERT INTO dividends 
            (id, symbol, amount,  timestamp) 
            VALUES (?, ?, ?, ?)""", 
            dividends
        )
        db.commit()
        db.close()
        print("Closed database successfully")
    except sqlite3.Error as e:
        print(f"Error selecting data: {e}")
