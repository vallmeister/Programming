class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        dp = [False] * 10 ** 5
        dp[primeOne] = True
        dp[primeTwo] = True
        ans = 0
        for i in range(10 ** 5):
            if i >= primeOne:
                dp[i] = dp[i] or dp[i - primeOne]
            if i >= primeTwo:
                dp[i] = dp[i] or dp[i - primeTwo]
            if not dp[i]:
                ans = i
        return ans


s = Solution()
print(s.mostExpensiveItem(2, 5))
