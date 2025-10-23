class CacheWithExpiry:
    def __init__(self):
        self.cache = {}
        self.expiry = {}

    def set(self, key, value, ttl, timestamp):
        self.cache[key] = value
        self.expiry[key] = timestamp + ttl

    def get(self, key, timestamp):
        if key not in self.cache:
            return None

        if timestamp >= self.expiry[key]:
            del self.cache[key]
            del self.expiry[key]
            return None

        return self.cache[key]

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.expiry[key]

    def cleanup(self, timestamp):
        keys_to_delete = []
        for key, expiry_time in self.expiry.items():
            if timestamp >= expiry_time:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del self.cache[key]
            del self.expiry[key]
