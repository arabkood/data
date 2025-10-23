from collections import defaultdict, deque


class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(deque)

    def allow_request(self, user_id, timestamp):
        # Remove old requests outside the time window
        while self.requests[user_id] and self.requests[user_id][0] <= timestamp - self.time_window:
            self.requests[user_id].popleft()

        # Check if we can allow this request
        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(timestamp)
            return True

        return False
