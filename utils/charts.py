import matplotlib.pyplot as plt
import uuid

def price_comparison_chart(stock1, stock2):
    labels = [stock1["symbol"], stock2["symbol"]]
    prices = [stock1["price"], stock2["price"]]

    plt.figure()
    plt.bar(labels, prices)
    plt.title("Stock Price Comparison")

    file = f"chart_{uuid.uuid4().hex}.png"
    plt.savefig(file)
    plt.close()
    return file
