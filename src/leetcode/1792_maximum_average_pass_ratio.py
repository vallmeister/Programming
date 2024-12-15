from heapq import heappush, heappop
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for passing, total in classes:
            heappush(heap, (-self.get_change(passing, total), total, passing))
        for _ in range(extraStudents):
            _, total, passing = heappop(heap)
            total += 1
            passing += 1
            heappush(heap, (-self.get_change(passing, total), total, passing))
        return sum(passing / total for _, total, passing in heap) / len(classes)

    def get_change(self, passing, total):
        return (passing + 1) / (total + 1) - passing / total


s = Solution()
print(s.maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
print(s.maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))
