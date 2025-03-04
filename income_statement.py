import sqlite3
import time
import json
from ulid import ULID

def get_income_statement(ticker, freq="quarterly"):
    try:
        db = sqlite3.connect("database/alexandria.db")
        print("Opened database successfully")
        cursor = db.cursor()

        yfinance_income_statements = ticker.get_income_stmt(as_dict=True, freq=freq)
        
        income_statements = [] 

        for key, value in yfinance_income_statements.items():
            new_ulid = ULID()
            time.sleep(0.001)

            cursor.execute("""
                SELECT symbol, timestamp
                FROM income_statements
                WHERE symbol = ?
                AND timestamp = ?
                AND freq = ?""",
                (ticker.ticker, key.to_pydatetime(), freq)
            )

            rows = cursor.fetchone()
            print(rows)

            if rows is None:
                income_statements.append((
                    bytes(new_ulid), 
                    ticker.ticker, 
                    json.dumps(value), 
                    freq, 
                    key.to_pydatetime()
                ))
            else:
                print("Balance sheet exist.")

        cursor.executemany("""
            INSERT INTO income_statements 
            (id, symbol, data, freq, timestamp) 
            VALUES (?, ?, ?, ?, ?)""", 
            income_statements
        )
        db.commit()
        db.close()
        print("Closed database successfully")
    except sqlite3.Error as e:
        print(f"Error selecting data: {e}")

