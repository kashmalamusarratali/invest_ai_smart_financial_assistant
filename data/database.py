import sqlite3
from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_data (
        symbol TEXT PRIMARY KEY,
        name TEXT,
        price REAL,
        sector TEXT
    )
    """)

    cursor.executemany("""
    INSERT OR IGNORE INTO stock_data VALUES (?, ?, ?, ?)
    """, [
        ("AAPL", "Apple Inc.", 179.32, "Technology"),
        ("MSFT", "Microsoft", 310.25, "Technology"),
        ("TSLA", "Tesla Inc.", 215.45, "Automotive"),
        ("F", "Ford", 142.10, "Automotive"),
        ("AMZN", "Amazon", 131.20, "E-commerce")
    ])

    conn.commit()
    conn.close()
