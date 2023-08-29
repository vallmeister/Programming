class Solution:
    # Can be further optimized by only using the last dp[i] instead of storing the whole array resulting in O(1) space
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        dp = [0] * (n + 1)
        for c in customers:
            if c == 'N':
                dp[n] += 1
        min_penalty = dp[n]
        hour = n
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1 if customers[i] == 'Y' else dp[i + 1] - 1
            if dp[i] <= min_penalty:
                min_penalty = dp[i]
                hour = i
        return hour


s = Solution()
print(s.bestClosingTime("YYNY"))
print(s.bestClosingTime("NNNNN"))
print(s.bestClosingTime("YYYY"))
print(s.bestClosingTime('YN'))
