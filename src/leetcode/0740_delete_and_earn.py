from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        scores = defaultdict(int)
        for num in nums:
            scores[num] += num

        dp = [0] * (10 ** 4 + 1)
        for i in range(1, 10 ** 4 + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + scores[i])

        return dp[-1]


s = Solution()
print(s.deleteAndEarn([3, 4, 2]))
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
