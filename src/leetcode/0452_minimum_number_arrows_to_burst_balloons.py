from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        xs, xe = points[0]
        for zs, ze in points[1:]:
            if xe < zs:
                arrows += 1
                xs, xe = zs, ze
            else:
                xs = max(xs, zs)
                xe = min(xe, ze)
        return arrows


s = Solution()
print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
