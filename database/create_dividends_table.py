import sqlite3

def run():
    try:
        db = sqlite3.connect("database/alexandria.db")
        print("Opened database successfully")
        cursor = db.cursor()

        cursor.execute("""
            create table if not exists dividends (
                id blob primary key, 
                symbol text not null,
                amount real,
                timestamp text
            )
        """)
        
        db.commit()
        print("Created table successfully")
        db.close()
        print("Closed database successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
