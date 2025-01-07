import sqlite3
import time
import json
from ulid import ULID

def get_balance_sheet(ticker, freq="quarterly"):
    db = sqlite3.connect("src/database/yfinance.db")
    print("Opened database successfully")
    cursor = db.cursor()

    balance_sheet = ticker.get_balance_sheet(as_dict=True, freq=freq)

    for key, value in balance_sheet.items():
        print(f"Key: {key}, Value: {value}")
        new_ulid = ULID()
        time.sleep(0.001)

        print(f"ULID(): {new_ulid}")
        print(f"str(ulid): {str(new_ulid)}")
        print(f"bytes(ulid): {bytes(new_ulid)}")
        print(f"ulid.timestamp: {new_ulid.timestamp}")
        print(f"ulid.datetime: {new_ulid.datetime}")

        cursor.execute("""
            INSERT INTO balance_sheets 
            (id, symbol, data, freq, timestamp) 
            VALUES (?, ?, ?, ?, ?)""", 
            (bytes(new_ulid), ticker.ticker, json.dumps(value), freq, key.to_pydatetime()))

     
    db.commit()

    db.close()
    print("Closed database successfully")
