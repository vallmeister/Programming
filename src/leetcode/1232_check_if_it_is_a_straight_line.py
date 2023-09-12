from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        last_x, last_y = coordinates[0]
        curr_x, curr_y = coordinates[1]
        dx, dy = curr_x - last_x, curr_y - last_y
        for i in range(2, len(coordinates)):
            last_x, last_y = curr_x, curr_y
            curr_x, curr_y = coordinates[i]
            if (curr_x - last_x) % dx != 0 or (curr_y - last_y) % dy != 0:
                return False
        return True


s = Solution()
print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(s.checkStraightLine([[2, 4], [2, 5], [2, 8]]))
