import random
import time
from typing import List
from src.engine.order import Order

class OrderGenerator:
    def __init__(
        self,
        num_orders: int,
        base_price: float = 100.0,
        price_volatility: float = 2.0,
        max_quantity: int = 10,
        seed: int = None,
    ):
        self.num_orders = num_orders
        self.base_price = base_price
        self.price_volatility = price_volatility
        self.max_quantity = max_quantity
        self.current_time = 0
        self.order_id_counter = 1
        if seed is not None:
            random.seed(seed)

    def generate_random_orders(self) -> List[Order]:
        orders = []
        for _ in range(self.num_orders):
            side = random.choice(["buy", "sell"])
            price = round(
                random.gauss(self.base_price, self.price_volatility), 2
            )
            quantity = random.randint(1, self.max_quantity)
            timestamp = self.current_time
            self.current_time += random.expovariate(1.0)  # Random time spacing

            order = Order(
                order_id=self.order_id_counter,
                side=side,
                price=price,
                quantity=quantity,
                timestamp=timestamp,
            )
            orders.append(order)
            self.order_id_counter += 1
        return orders
