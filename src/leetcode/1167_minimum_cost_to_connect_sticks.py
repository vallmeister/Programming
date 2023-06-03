from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        costs = 0
        while len(sticks) > 1:
            fst = heappop(sticks)
            snd = heappop(sticks)
            costs += fst + snd
            heappush(sticks, fst + snd)
        return costs


s = Solution()
print(s.connectSticks([2, 4, 3]))
print(s.connectSticks([1, 8, 3, 5]))
print(s.connectSticks([5]))
