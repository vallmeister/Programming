from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        tmp = []
        for i, row in enumerate(grid):
            tmp.extend(list(sorted(row, reverse=True))[:limits[i]])
        return sum(sorted(tmp, reverse=True)[:k])


s = Solution()
print(s.maxSum(grid=[[1, 2], [3, 4]], limits=[1, 2], k=2))
print(s.maxSum(grid=[[5, 3, 7], [8, 2, 6]], limits=[2, 2], k=3))
