class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        n = len(prob)
        dp = [1.0, 0]
        for c in range(1, n + 1):
            new_dp = [0] * (c + 2)
            for k in range(c, -1, -1):
                if k == 0:
                    new_dp[k] = dp[k] * (1 - prob[c - 1])
                else:
                    new_dp[k] = dp[k] * (1 - prob[c - 1]) + dp[k - 1] * prob[c - 1]
            dp = new_dp
        return dp[target]


s = Solution()
print(s.probabilityOfHeads([0.4], 1))
print(s.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 0))
print(s.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 2))
