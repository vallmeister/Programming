from heapq import heappush, heappop
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        monsters_killed = 0
        curr_time = 0
        n = len(dist)
        for i in range(n):
            heappush(heap, dist[i] / speed[i])
        while heap and curr_time < heap[0]:
            heappop(heap)
            monsters_killed += 1
            curr_time += 1
        return monsters_killed


s = Solution()
print(s.eliminateMaximum([1, 3, 4], speed=[1, 1, 1]))
print(s.eliminateMaximum([1, 1, 2, 3], speed=[1, 1, 1, 1]))
print(s.eliminateMaximum([3, 2, 4], speed=[5, 3, 2]))
print(s.eliminateMaximum([4, 3, 4], [1, 1, 2]))
