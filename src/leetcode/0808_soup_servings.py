import math
from collections import defaultdict


class Solution:
    def soupServings(self, n: int) -> float:
        n = math.ceil(n / 25)
        dp = defaultdict(float)

        def memo(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            elif (a, b) in dp:
                return dp[(a, b)]

            dp[(a, b)] = (
                                 memo(a - 4, b)
                                 + memo(a - 3, b - 1)
                                 + memo(a - 2, b - 2)
                                 + memo(a - 1, b - 3)
                         ) / 4.0

            return dp[(a, b)]

        for k in range(1, n + 1):
            if memo(k, k) > 1 - 1e-5:
                return 1.0
        return memo(n, n)


s = Solution()
print(s.soupServings(50))
print(s.soupServings(100))
print(s.soupServings(660295675))
