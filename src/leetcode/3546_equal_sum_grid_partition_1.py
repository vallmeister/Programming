from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        return self.can_partition([sum(row) for row in grid]) or self.can_partition(
            [sum(grid[i][j] for i in range(n)) for j in range(m)])

    def can_partition(self, nums):
        total = sum(nums)
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if total - curr_sum == curr_sum:
                return True
        return False


s = Solution()
print(s.canPartitionGrid(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid(grid=[[1, 3], [2, 4]]))
print(s.canPartitionGrid(grid=[[54756, 54756]]))
