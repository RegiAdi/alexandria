import sqlite3
import time
import json
from ulid import ULID

def get_cash_flow(ticker, freq="quarterly"):
    try:
        db = sqlite3.connect("database/alexandria.db")
        print("Opened database successfully")
        cursor = db.cursor()

        yfinance_cash_flow = ticker.get_cash_flow(as_dict=True, freq=freq)
        
        cash_flows = [] 

        for key, value in yfinance_cash_flow.items():
            new_ulid = ULID()
            time.sleep(0.001)

            cursor.execute("""
                SELECT symbol, timestamp
                FROM cash_flows
                WHERE symbol = ?
                AND timestamp = ?
                AND freq = ?""",
                (ticker.ticker, key.to_pydatetime(), freq)
            )

            rows = cursor.fetchone()
            print(rows)

            if rows is None:
                cash_flows.append((
                    bytes(new_ulid), 
                    ticker.ticker, 
                    json.dumps(value), 
                    freq, 
                    key.to_pydatetime()
                ))
            else:
                print("Cash Flow exist.")

        cursor.executemany("""
            INSERT INTO cash_flows 
            (id, symbol, data, freq, timestamp) 
            VALUES (?, ?, ?, ?, ?)""", 
            cash_flows
        )
        db.commit()
        db.close()
        print("Closed database successfully")
    except sqlite3.Error as e:
        print(f"Error selecting data: {e}")

