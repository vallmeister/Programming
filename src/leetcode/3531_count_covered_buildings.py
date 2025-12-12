import bisect
from collections import defaultdict
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_positions = defaultdict(list)
        col_positions = defaultdict(list)
        for x, y in buildings:
            row_positions[y].append(x)
            col_positions[x].append(y)
        for row in row_positions.values():
            row.sort()
        for col in col_positions.values():
            col.sort()
        ans = 0
        for x, y in buildings:
            row = row_positions[y]
            mm = len(row)
            i = bisect.bisect_left(row, x)
            col = col_positions[x]
            nn = len(col)
            j = bisect.bisect_left(col, y)
            if 0 < i < mm - 1 and 0 < j < nn - 1:
                ans += 1
        return ans


s = Solution()
print(s.countCoveredBuildings(n=3, buildings=[[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
print(s.countCoveredBuildings(n=3, buildings=[[1, 1], [1, 2], [2, 1], [2, 2]]))
