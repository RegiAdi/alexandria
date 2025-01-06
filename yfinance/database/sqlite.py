import sqlite3

def get_db():
    db = sqlite3.connect("database/alexandria.db")
    print("Opened database successfully")

    return db.cursor()

def close_db(db):
    db.close()
    print("Closed database successfully")
