from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal = []
        vertical = []
        for sx, sy, ex, ey in rectangles:
            horizontal.append((sx, ex))
            vertical.append((sy, ey))
        horizontal.sort()
        vertical.sort()
        return self.at_least_two_cuts(horizontal) or self.at_least_two_cuts(vertical)

    def at_least_two_cuts(self, intervals):
        prev_start, prev_end = intervals[0]
        count = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                prev_end = max(prev_end, end)
            else:
                prev_start, prev_end = start, end
                count += 1
        return count >= 2


s = Solution()
print(s.checkValidCuts(n=5, rectangles=[[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))
print(s.checkValidCuts(n=4, rectangles=[[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))
print(s.checkValidCuts(n=4, rectangles=[[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))
