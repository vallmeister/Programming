import math
from functools import cache


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        @cache
        def recursive(idx, lst_value):
            if idx == len(nums):
                return 0
            elif nums[idx] <= lst_value:
                return recursive(idx + 1, lst_value)
            else:
                return max(recursive(idx + 1, lst_value), 1 + recursive(idx + 1, nums[idx]))

        def dynamic_programming():
            n = len(nums)
            dp = [1] * n

            for i in reversed(range(n)):
                for j in range(i + 1, n):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], 1 + dp[j])

            return max(dp)

        return dynamic_programming()


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
