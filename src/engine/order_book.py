from collections import defaultdict, deque
from sortedcontainers import SortedDict
from .order import Order

class OrderBook:
    def __init__(self):
        self.bids = SortedDict(lambda x: -x)  # Max-heap behavior
        self.asks = SortedDict()             # Min-heap behavior
        self.order_id_map = {}
        self.trade_log = []

    def add_order(self, order: Order):
        book = self.bids if order.side == "buy" else self.asks
        if order.price not in book:
            book[order.price] = deque()
        book[order.price].append(order)
        self.order_id_map[order.order_id] = order
        self.match()

    def match(self):
        while self.bids and self.asks:
            best_bid = next(iter(self.bids))
            best_ask = next(iter(self.asks))
            if best_bid >= best_ask:
                bid_order = self.bids[best_bid][0]
                ask_order = self.asks[best_ask][0]

                trade_qty = min(bid_order.quantity, ask_order.quantity)
                self.trade_log.append({
                    "price": best_ask,
                    "quantity": trade_qty,
                    "buy_id": bid_order.order_id,
                    "sell_id": ask_order.order_id
                })

                bid_order.quantity -= trade_qty
                ask_order.quantity -= trade_qty

                if bid_order.quantity == 0:
                    self.bids[best_bid].popleft()
                    if not self.bids[best_bid]:
                        del self.bids[best_bid]

                if ask_order.quantity == 0:
                    self.asks[best_ask].popleft()
                    if not self.asks[best_ask]:
                        del self.asks[best_ask]
            else:
                break

    def cancel_order(self, order_id):
        order = self.order_id_map.get(order_id)
        if not order:
            return False
        book = self.bids if order.side == "buy" else self.asks
        if order.price in book:
            queue = book[order.price]
            for i, o in enumerate(queue):
                if o.order_id == order_id:
                    del queue[i]
                    if not queue:
                        del book[order.price]
                    del self.order_id_map[order_id]
                    return True
        return False

    def print_order_book(self):
        print("\nOrder Book:")
        print("Bids:")
        for price, orders in self.bids.items():
            print(f"{price}: {[o.quantity for o in orders]}")
        print("Asks:")
        for price, orders in self.asks.items():
            print(f"{price}: {[o.quantity for o in orders]}")
