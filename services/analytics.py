from services.stocks import fetch_stock_price
from data.repository import get_sector_stocks

def compare_stocks(sym1, sym2):
    s1 = fetch_stock_price(sym1)
    s2 = fetch_stock_price(sym2)

    if not s1 or not s2:
        return None

    return {
        "stock_1": s1,
        "stock_2": s2,
        "price_difference": abs(s1["price"] - s2["price"])
    }

def sector_average(sector):
    prices = get_sector_stocks(sector)
    if not prices:
        return None
    return sum(prices) / len(prices)
