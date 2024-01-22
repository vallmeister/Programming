import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < math.inf else -1


s = Solution()
print(s.coinChange([1, 2, 5], amount=11))
print(s.coinChange([2], amount=3))
print(s.coinChange([1], amount=0))
print(s.coinChange([1, 2], 2))
