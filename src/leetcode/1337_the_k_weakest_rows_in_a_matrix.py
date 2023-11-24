from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for idx, row in enumerate(mat):
            # Optimize strength calculation by using binary search
            heappush(heap, (-sum(row), -idx))
            if len(heap) > k:
                heappop(heap)
        ans = deque()
        while heap:
            soldiers, idx = heappop(heap)
            ans.appendleft(-idx)
        return list(ans)


s = Solution()
print(s.kWeakestRows([[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]],
                     k=3))
print(s.kWeakestRows([[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]],
                     k=2))
