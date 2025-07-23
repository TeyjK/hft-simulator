from dataclasses import dataclass
import time

@dataclass
class Order:
    order_id: int
    timestamp: float
    side: str  # "buy" or "sell"
    price: float
    quantity: int

    def __init__(self, order_id, side, price, quantity, timestamp=None):
        self.order_id = order_id
        self.timestamp = timestamp if timestamp is not None else time.time()
        self.side = side.lower()
        self.price = price
        self.quantity = quantity
