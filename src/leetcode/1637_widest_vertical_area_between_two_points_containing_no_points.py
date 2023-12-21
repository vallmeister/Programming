from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort()
        prev, _ = points[0]
        for x, _ in points[1:]:
            ans = max(ans, x - prev)
            prev = x
        return ans


s = Solution()
print(s.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
print(s.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
