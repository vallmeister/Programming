from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        curr_x, curr_y = points[0]
        for x, y in points[1:]:
            ans += max(abs(x - curr_x), abs(y - curr_y))
            curr_x, curr_y = x, y
        return ans


s = Solution()
print(s.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
print(s.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
