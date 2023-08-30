from typing import List
from heapq import heappop, heappush


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x: (x[1], -x[0]))
        heap = []
        for _ in range(k):
            while projects and projects[0][1] <= w:
                profit, capital = projects.pop(0)
                heappush(heap, -profit)
            if not heap:
                break
            w -= heappop(heap)
        return w


s = Solution()
print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
print(s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
