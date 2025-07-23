from collections import deque
from sortedcontainers import SortedDict
from src.engine.order import Order

class OrderBook:
    def __init__(self):
        self.bids = SortedDict(lambda x: -x)  # descending order for bids
        self.asks = SortedDict()               # ascending order for asks
        self.order_id_map = {}
        self.trade_log = []

    def add_order(self, order: Order):
        book = self.bids if order.side == "buy" else self.asks
        if order.price not in book:
            book[order.price] = deque()
        book[order.price].append(order)
        self.order_id_map[order.order_id] = order

    def match(self):
        matched_trades = []

        while self.bids and self.asks:
            best_bid = next(iter(self.bids))
            best_ask = next(iter(self.asks))

            if best_bid >= best_ask:
                bid_order = self.bids[best_bid][0]
                ask_order = self.asks[best_ask][0]

                trade_qty = min(bid_order.quantity, ask_order.quantity)

                trade = {
                    "price": best_ask,
                    "quantity": trade_qty,
                    "buy_id": bid_order.order_id,
                    "sell_id": ask_order.order_id,
                    "buy_order_price": bid_order.price,
                    "sell_order_price": ask_order.price
                }
                matched_trades.append(trade)
                self.trade_log.append(trade)

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

        return matched_trades