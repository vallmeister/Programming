from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def memo(s):
            if s == target:
                return 1
            elif s > target:
                return 0
            res = 0
            for num in nums:
                res += memo(s + num)
            return res

        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for num in nums:
                if i + num > target:
                    continue
                dp[i + num] += dp[i]

        return dp[target]


sol = Solution()
print(sol.combinationSum4([1, 2, 3], 4))
print(sol.combinationSum4([9], 3))
print(sol.combinationSum4([4, 2, 1], 32))
