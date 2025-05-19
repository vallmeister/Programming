class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if 0 <= i - maxPts < k:
                s -= dp[i - maxPts]
        return round(sum(dp[k:]), 5)


ssol = Solution()
print(ssol.new21Game(10, 1, 10))
print(ssol.new21Game(6, 1, 10))
print(ssol.new21Game(21, 17, 10))
print(ssol.new21Game(421, 400, 47))
print(ssol.new21Game(9811, 8776, 1096))
