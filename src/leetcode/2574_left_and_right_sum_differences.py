from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
        right_sum = [0] * n
        for i in reversed(range(n - 1)):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]
        ans = [0] * n
        for i in range(n):
            ans[i] = abs(left_sum[i] - right_sum[i])
        return ans
