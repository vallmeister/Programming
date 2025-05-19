import math
from functools import cache
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @cache
        def memo(i, prev_color, hoods):
            if hoods < 0 or i >= m and hoods != 0:
                return math.inf
            elif i >= m:
                return 0
            elif houses[i] != 0:
                return memo(i + 1, houses[i], hoods - 1) if houses[i] != prev_color else memo(i + 1, houses[i], hoods)
            ans = []
            for color in range(1, n + 1):
                total = memo(i + 1, color, hoods - 1) if color != prev_color else memo(i + 1, color, hoods)
                ans.append(total + cost[i][color - 1])
            return min(ans)

        res = memo(0, 0, target)
        return res if res < math.inf else -1


s = Solution()
print(s.minCost(houses=[0, 0, 0, 0, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2, target=3))
print(s.minCost(houses=[0, 2, 1, 2, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2, target=3))
print(s.minCost(houses=[3, 1, 2, 3], cost=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], m=4, n=3, target=3))
