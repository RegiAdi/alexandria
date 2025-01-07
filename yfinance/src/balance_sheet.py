import sqlite3
import time
import json
from ulid import ULID

def get_balance_sheet(ticker, freq="quarterly"):
    try:
        db = sqlite3.connect("src/database/yfinance.db")
        print("Opened database successfully")
        cursor = db.cursor()

        yfinance_balance_sheet = ticker.get_balance_sheet(as_dict=True, freq=freq)
        
        balance_sheets = [] 

        for key, value in yfinance_balance_sheet.items():
            # print(f"Key: {key}, Value: {value}")
            new_ulid = ULID()
            time.sleep(0.001)

            cursor.execute("""
                SELECT symbol, timestamp
                FROM balance_sheets
                WHERE symbol = ?
                AND timestamp = ?
                AND freq = ?""",
                (ticker.ticker, key.to_pydatetime(), freq)
            )

            rows = cursor.fetchone()
            print(rows)

            if rows is None:
                balance_sheets.append((
                    bytes(new_ulid), 
                    ticker.ticker, 
                    json.dumps(value), 
                    freq, 
                    key.to_pydatetime()
                ))
            else:
                print("Balance sheet exist.")

        cursor.executemany("""
            INSERT INTO balance_sheets 
            (id, symbol, data, freq, timestamp) 
            VALUES (?, ?, ?, ?, ?)""", 
            balance_sheets
        )
        db.commit()
        db.close()
        print("Closed database successfully")
    except sqlite3.Error as e:
        print(f"Error selecting data: {e}")

