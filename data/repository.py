from data.database import get_connection

def get_stock(symbol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT symbol, name, price, sector FROM stock_data WHERE symbol = ?",
        (symbol.upper(),)
    )
    row = cursor.fetchone()
    conn.close()
    return row

def get_sector_stocks(sector):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT price FROM stock_data WHERE sector = ?",
        (sector,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]
