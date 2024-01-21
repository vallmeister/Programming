from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1000
        for i in range(1, n):
            for j in range(i + 1, n):
                ans = min(ans, nums[i] + nums[j] + nums[0])
        return ans


s = Solution()
print(s.minimumCost([1, 2, 3, 12]))
print(s.minimumCost([5, 4, 3]))
print(s.minimumCost([10, 3, 1, 1]))
