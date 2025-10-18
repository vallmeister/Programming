import math
from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        dp = [math.inf] * n
        dp[-1] = 0
        for i in reversed(range(n - 1)):
            for k in range(1, min(maxJump + 1, n - i)):
                if coins[i + k] == -1:
                    continue
                dp[i] = min(dp[i], coins[i] + dp[i + k])
        if dp[0] == math.inf:
            return []

        ans = [1]
        min_cost = dp[0]
        while ans[-1] != n:
            i = ans[-1]
            min_cost -= coins[i - 1]
            for k in range(1, min(maxJump + 1, n - i + 1)):
                if min_cost == dp[i + k - 1]:
                    ans.append(i + k)
                    break
        return ans


s = Solution()
print(s.cheapestJump(coins=[1, 2, 4, -1, 2], maxJump=2))
print(s.cheapestJump(coins=[1, 2, 4, -1, 2], maxJump=1))
print(s.cheapestJump([0, -1, -1, -1, -1, -1], 5))
