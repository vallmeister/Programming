from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        dp = [1] * n
        envelopes.sort()
        for i in range(n):
            w_i, h_i = envelopes[i]
            for j in range(i):
                w_j, h_j = envelopes[j]
                if w_i > w_j and h_i > h_j:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
