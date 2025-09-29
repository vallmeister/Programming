from functools import cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @cache
        def memo(i, j):
            tmp = values[i] * values[j]
            if i + 2 > j:
                return 0
            elif i + 2 == j:
                return tmp * values[i + 1]
            ans = []
            for k in range(i + 1, j):
                ans.append(tmp * values[k] + memo(i, k) + memo(k, j))
            return min(ans)

        return memo(0, n - 1)


s = Solution()
print(s.minScoreTriangulation([1, 2, 3]))
print(s.minScoreTriangulation([3, 7, 4, 5]))
print(s.minScoreTriangulation([1, 3, 1, 4, 1, 5]))
