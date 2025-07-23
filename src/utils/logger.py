import csv
import os

class Logger:
    def __init__(self, order_log_path="logs/orders.csv", trade_log_path="logs/trades.csv"):
        os.makedirs(os.path.dirname(order_log_path), exist_ok=True)
        os.makedirs(os.path.dirname(trade_log_path), exist_ok=True)

        self.order_log_path = order_log_path
        self.trade_log_path = trade_log_path

        # Initialize order log CSV
        if not os.path.exists(order_log_path):
            with open(order_log_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["order_id", "timestamp", "side", "price", "quantity"])

        # Initialize trade log CSV
        if not os.path.exists(trade_log_path):
            with open(trade_log_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["price", "quantity", "buy_id", "sell_id", "timestamp", "buy_order_price", "sell_order_price"])

    def log_order(self, order):
        with open(self.order_log_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                order.order_id,
                order.timestamp,
                order.side,
                order.price,
                order.quantity
            ])

    def log_trade(self, trade):
        with open(self.trade_log_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                trade["price"],
                trade["quantity"],
                trade["buy_id"],
                trade["sell_id"],
                trade.get("timestamp", ""),
                trade.get("buy_order_price", ""),
                trade.get("sell_order_price", "")
            ])
