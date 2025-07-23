from src.simulator.order_generator import OrderGenerator

gen = OrderGenerator(num_orders=10, seed=42)
orders = gen.generate_random_orders()

for order in orders:
    print(f"ID: {order.order_id}, Side: {order.side}, Price: {order.price:.2f}, Qty: {order.quantity}, Time: {order.timestamp:.2f}")