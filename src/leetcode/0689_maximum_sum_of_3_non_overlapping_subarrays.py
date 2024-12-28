import math
from functools import cache
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        window = sum((nums[:k]))
        sums = [0] * n
        sums[0] = window
        for i in range(1, n):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1]

        @cache
        def dp(idx, remaining):
            if remaining == 0:
                return 0
            elif idx >= n:
                return -math.inf
            return max(dp(idx + 1, remaining), sums[idx] + dp(idx + k, remaining - 1))

        indices = []

        def dfs(idx, remaining):
            if remaining == 0 or idx >= n:
                return
            with_curr = sums[idx] + dp(idx + k, remaining - 1)
            without_curr = dp(idx + 1, remaining)
            if with_curr >= without_curr:
                indices.append(idx)
                dfs(idx + k, remaining - 1)
            else:
                dfs(idx + 1, remaining)

        dfs(0, 3)
        return indices


s = Solution()
print(s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
