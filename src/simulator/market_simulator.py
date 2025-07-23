from src.engine.order_book import OrderBook
from src.simulator.order_generator import OrderGenerator
from src.simulator.latency_simulator import LatencySimulator
from src.utils.logger import Logger

class MarketSimulator:
    def __init__(self, num_orders=1000, base_price=100.0, min_latency_ms=1, max_latency_ms=10):
        self.order_book = OrderBook()
        self.order_generator = OrderGenerator(num_orders=num_orders, base_price=base_price)
        self.latency_simulator = LatencySimulator(min_latency_ms, max_latency_ms)
        self.logger = Logger()
        self.trades = []

    def run(self):
        orders = self.order_generator.generate_random_orders()
        for order in orders:
            self.logger.log_order(order)  # Log order immediately
            self.latency_simulator.add_order(order)

        while self.latency_simulator.has_orders():
            delivery_time, delayed_order = self.latency_simulator.pop_next_order()
            self.order_book.add_order(delayed_order)
            matched_trades = self.order_book.match()

            for trade in matched_trades:
                # Add timestamp to trade for logging (use delivery_time or current time)
                trade["timestamp"] = delivery_time
                self.logger.log_trade(trade)

            self.trades.extend(matched_trades)

        self.print_summary()

    def print_summary(self):
        print(f"Total trades executed: {len(self.trades)}")
        for trade in self.trades[:10]:
            print(trade)

if __name__ == "__main__":
    sim = MarketSimulator(num_orders=100)
    sim.run()