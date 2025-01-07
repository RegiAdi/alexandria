import sqlite3

try:
    db = sqlite3.connect("src/database/yfinance.db")
    print("Opened database successfully")
    cursor = db.cursor()

    cursor.execute("""
        create table if not exists balance_sheets (
            id blob primary key, 
            symbol text not null,
            data text,
            freq text,
            timestamp text
        )
    """)
    
    db.commit()
    db.close()
    print("Closed database successfully")
except sqlite3.Error as e:
    print(f"Error creating table: {e}")
