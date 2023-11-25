from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        delta_x = x1 - x0
        delta_y = y1 - y0
        x0, y0 = x1, y1
        for x1, y1 in coordinates[2:]:
            if (x1 - x0) * delta_y != (y1 - y0) * delta_x:
                return False
        return True


s = Solution()
print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(s.checkStraightLine([[2, 4], [2, 5], [2, 8]]))
