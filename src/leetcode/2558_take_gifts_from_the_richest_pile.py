from heapq import heappush, heappop
from math import sqrt, floor
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heappush(heap, -gift)
        for _ in range(k):
            gift = -heappop(heap)
            root = floor(sqrt(gift))
            heappush(heap, -root)
        return sum(-gift for gift in heap)


s = Solution()
print(s.pickGifts([25, 64, 9, 4, 100], 4))
