import random
import heapq

class LatencySimulator:
    def __init__(self, min_latency_ms=1, max_latency_ms=10):
        self.min_latency = min_latency_ms / 1000  # convert to seconds
        self.max_latency = max_latency_ms / 1000
        self.event_queue = []  # min-heap to simulate delayed events (timestamp, order)

    def add_order(self, order):
        latency = random.uniform(self.min_latency, self.max_latency)
        delivery_time = order.timestamp + latency
        heapq.heappush(self.event_queue, (delivery_time, order))

    def get_next_order(self):
        if self.event_queue:
            delivery_time, order = self.event_queue[0]
            return delivery_time, order
        return None, None

    def pop_next_order(self):
        if self.event_queue:
            return heapq.heappop(self.event_queue)
        return None, None

    def has_orders(self):
        return len(self.event_queue) > 0