class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [1] * (n + 1)
        prev = {}
        for i in reversed(range(n)):
            dp[i] = 2 * dp[i + 1]
            c = s[i]
            if c in prev:
                dp[i] -= dp[prev[c] + 1]
            prev[c] = i
            dp[i] %= MOD
        return (dp[0] - 1) % MOD


s = Solution()
print(s.distinctSubseqII('abc'))
