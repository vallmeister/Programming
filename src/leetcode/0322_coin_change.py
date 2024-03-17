import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                for coin in coins:
                    if coin > i:
                        continue
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] < math.inf else -1


s = Solution()
print(s.coinChange([1, 2, 5], amount=11))
print(s.coinChange([2], amount=3))
print(s.coinChange([1], amount=0))
print(s.coinChange([1, 2], 2))
