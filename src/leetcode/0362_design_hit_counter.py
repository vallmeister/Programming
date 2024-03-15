from heapq import heappush, heappop


class HitCounter:

    def __init__(self):
        self.hits = []
        self.count = 0

    def hit(self, timestamp: int) -> None:
        heappush(self.hits, timestamp)
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            heappop(self.hits)
            self.count -= 1
        return self.count
