from collections import defaultdict
from heapq import heappush, heappop


class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] +=score

    def top(self, K: int) -> int:
        heap = []
        res = 0
        for score in self.scores.values():
            heappush(heap, score)
            res += score
            if len(heap) > K:
                res -= heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
