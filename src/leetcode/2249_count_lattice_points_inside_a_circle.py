import math
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        x_min = y_min = 200
        x_max = y_max = 0
        for x, y, r in circles:
            x_min = min(x_min, x - r)
            y_min = min(y_min, y - r)
            x_max = max(x_max, x + r)
            y_max = max(y_max, y + r)
        ans = 0
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                if self.circles_contain(circles, x, y):
                    ans += 1
        return ans

    def circles_contain(self, circles, x, y):
        for cx, cy, r in circles:
            if math.sqrt((x - cx) ** 2 + (y - cy) ** 2) <= r:
                return True
        return False


s = Solution()
print(s.countLatticePoints([[2, 2, 1]]))
print(s.countLatticePoints([[2, 2, 2], [3, 4, 1]]))
