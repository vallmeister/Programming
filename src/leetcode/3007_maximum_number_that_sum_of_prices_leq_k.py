from bisect import bisect_right
from math import ceil, log2


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        def price(n):
            p = 0
            for i in range(1, ceil(log2(n)) + 2):
                if i % x == 0:
                    p += (n + 1) // (1 << i) * (1 << (i - 1))
                    p += max(0, (n + 1) % (1 << i) - (1 << (i - 1)))
            return p

        return bisect_right(range(1, 1 << 63), k, key=price)


s = Solution()
print(s.findMaximumNumber(9, 1))
print(s.findMaximumNumber(7, 2))
