import math
from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        points.sort()
        slopes_intersections_count = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]

                dx = xj - xi
                dy = yj - yi
                if dx == 0:
                    slopes_intersections_count[math.inf][xi] += 1
                else:
                    m = dy / dx
                    c = yi - m * xi
                    slopes_intersections_count[m][c] += 1
        for intersections_count in slopes_intersections_count.values():
            for i, count1 in enumerate(intersections_count.values()):
                for j, count2 in enumerate(intersections_count.values()):
                    if j <= i:
                        continue
                    ans += count1 * count2
        return ans


s = Solution()
print(s.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]))  # 2
print(s.countTrapezoids(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))  # 1
print(s.countTrapezoids([[-32, 12], [-32, -94], [-32, -15], [-30, 88]]))  # 0
print(s.countTrapezoids([[82, 7], [82, -9], [82, -52], [82, 78]]))  # 0
print(s.countTrapezoids([[55, 57], [-51, 57], [99, 57], [7, 57]]))  # 0
print(s.countTrapezoids([[71, -89], [-75, -89], [-9, 11], [-24, -89], [-51, -89], [-77, -89], [42, 11]]))  # 10
