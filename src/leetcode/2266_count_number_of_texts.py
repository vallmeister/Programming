class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        MOD = 10 ** 9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] += dp[i - 1]
            if i - 2 >= 0 and pressedKeys[i - 2] == pressedKeys[i - 1]:
                dp[i] += dp[i - 2]
                if i - 3 >= 0 and pressedKeys[i - 3] == pressedKeys[i - 1]:
                    dp[i] += dp[i - 3]
                    if i - 4 >= 0 and pressedKeys[i - 4] in '79' and pressedKeys[i - 4] == pressedKeys[i - 1]:
                        dp[i] += dp[i - 4]
            dp[i] %= MOD
        return dp[-1]


s = Solution()
print(s.countTexts("22233"))
print(s.countTexts("222222222222222222222222222222222222"))
print(s.countTexts("444479999555588866"))
