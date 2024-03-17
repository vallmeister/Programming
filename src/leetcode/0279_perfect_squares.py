import math
from functools import cache


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            sq = i * i
            squares.append(sq)
            dp[sq] = 1
        for i in range(n):
            for sq in squares:
                if i + sq > n:
                    continue
                dp[i + sq] = min(dp[i + sq], dp[i] + 1)
        return dp[n]


s = Solution()
print(s.numSquares(1))
print(s.numSquares(12))
print(s.numSquares(13))
