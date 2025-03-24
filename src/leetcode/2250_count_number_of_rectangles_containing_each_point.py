import bisect
from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        heights = [[] for _ in range(101)]
        for l, h in rectangles:
            heights[h].append(l)
        for i in range(101):
            heights[i].sort()
        ans = []
        for l, h in points:
            tmp = 0
            for i in range(h, 101):
                ip = bisect.bisect_left(heights[i], l)
                tmp += len(heights[i]) - ip
            ans.append(tmp)
        return ans


s = Solution()
print(s.countRectangles([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]]))
print(s.countRectangles(rectangles=[[1, 1], [2, 2], [3, 3]], points=[[1, 3], [1, 1]]))
print(s.countRectangles([[7, 1], [2, 6], [1, 4], [5, 2], [10, 3], [2, 4], [5, 9]],
                        [[10, 3], [8, 10], [2, 3], [5, 4], [8, 5], [7, 10], [6, 6], [3, 6]]))
