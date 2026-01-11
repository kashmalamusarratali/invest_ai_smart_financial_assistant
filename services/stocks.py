from data.repository import get_stock

def fetch_stock_price(symbol):
    stock = get_stock(symbol)
    if not stock:
        return None
    return {
        "symbol": stock[0],
        "name": stock[1],
        "price": stock[2],
        "sector": stock[3]
    }
