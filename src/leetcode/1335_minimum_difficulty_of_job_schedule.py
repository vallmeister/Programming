import math
from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        @cache
        def dp(idx, curr_day, curr_max):
            if idx == len(jobDifficulty):
                if curr_day < d:
                    return math.inf
                return curr_max
            curr_max = max(curr_max, jobDifficulty[idx])
            return min(dp(idx + 1, curr_day, curr_max),
                       curr_max + dp(idx + 1, curr_day + 1, 0))

        return dp(0, 0, 0)


s = Solution()
print(s.minDifficulty([6, 5, 4, 3, 2, 1], d=2))
print(s.minDifficulty([9, 9, 9], d=4))
print(s.minDifficulty([1, 1, 1], d=3))
print(s.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))  # 843
