class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (n + 1) for _ in range(n)]
        dp[0][0] = 1 - prob[0]
        dp[0][1] = prob[0]
        for coin in range(1, n):
            for heads in range(coin + 2):
                dp[coin][heads] = dp[coin - 1][heads - 1] * prob[coin] + dp[coin - 1][heads] * (1 - prob[coin])

        return dp[n - 1][target]


s = Solution()
print(s.probabilityOfHeads([0.4], 1))
print(s.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 0))
print(s.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 2))
