from functools import cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        ps = [[] for _ in range(n)]
        for i in range(n):
            ps[i].append(0)
            s = 0
            for j in range(len(piles[i])):
                s += piles[i][j]
                ps[i].append(s)

        @cache
        def memo(i, left):
            if i >= n or left == 0:
                return 0
            ans = []
            for j in range(min(left, len(piles[i])) + 1):
                ans.append(memo(i + 1, left - j) + ps[i][j])
            return max(ans)

        return memo(0, k)


sol = Solution()
print(sol.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], k=2))
print(sol.maxValueOfCoins([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], k=7))
