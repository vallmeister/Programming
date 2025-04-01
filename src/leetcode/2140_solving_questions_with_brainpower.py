from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            dp[i] = max(dp[i + 1], points + dp[min(i + brainpower + 1, n)])
        return dp[0]
