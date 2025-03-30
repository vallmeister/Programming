from functools import cache
from typing import List


class Solution:
    # Editorial help => revisit
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]

        @cache
        def memo(left, right):
            if right - left == 1:
                return 0
            return cuts[right] - cuts[left] + min(memo(left, mid) + memo(mid, right) for mid in range(left + 1, right))

        return memo(0, len(cuts) - 1)


s = Solution()
print(s.minCost(n=7, cuts=[1, 3, 4, 5]))
print(s.minCost(n=9, cuts=[5, 6, 1, 4, 2]))
