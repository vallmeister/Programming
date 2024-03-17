from functools import cache
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def memo(i):
            if i >= n:
                return 0
            points, brainpower = questions[i]
            return max(memo(i + 1), points + memo(i + brainpower + 1))

        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            p, b = questions[i]
            dp[i] = max(dp[i + 1], p + dp[min(i + b + 1, n)])

        return dp[0]
