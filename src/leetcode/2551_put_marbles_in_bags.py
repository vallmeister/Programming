from heapq import heappush, heappop
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        min_heap = []
        max_heap = []
        for i in range(n - 1):
            heappush(max_heap, weights[i] + weights[i + 1])
            heappush(min_heap, -(weights[i] + weights[i + 1]))
            while len(min_heap) >= k:
                heappop(min_heap)
            while len(max_heap) >= k:
                heappop(max_heap)
        return sum(max_heap) + sum(min_heap)


s = Solution()
print(s.putMarbles(weights=[1, 3, 5, 1], k=2))
print(s.putMarbles(weights=[1, 3], k=2))
