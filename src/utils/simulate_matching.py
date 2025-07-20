from src.engine.order import Order
from src.engine.order_book import OrderBook

def run_simulation():
    ob = OrderBook()

    # Submit buy orders
    ob.add_order(Order(1, "buy", 100.0, 10))
    ob.add_order(Order(2, "buy", 101.0, 5))

    # Submit sell orders
    ob.add_order(Order(3, "sell", 99.0, 8))
    ob.add_order(Order(4, "sell", 102.0, 10))

    # Print order book state
    ob.print_order_book()

    # Print trades executed
    print("\nTrades executed:")
    for trade in ob.trade_log:
        print(trade)

if __name__ == "__main__":
    run_simulation()
