class LRUCache:
    cache = {}
    capacity = 0
    lru = [] # use deque

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.lru.append()
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            del self.cache[self.lru]
        self.cache[key] = value
        self.lru = key
