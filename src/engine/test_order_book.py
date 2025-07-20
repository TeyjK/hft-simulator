from order import Order
from order_book import OrderBook

ob = OrderBook()

# Add some orders
ob.add_order(Order(1, "buy", 100.0, 10))
ob.add_order(Order(2, "sell", 99.0, 5))
ob.add_order(Order(3, "sell", 101.0, 5))
ob.add_order(Order(4, "buy", 98.0, 5))

ob.print_order_book()

print("\nTrades:")
for t in ob.trade_log:
    print(t)
