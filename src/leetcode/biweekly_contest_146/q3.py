from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        m = len(rectangles)

        rectangles.sort(key=lambda x: (x[0], x[2]))
        vertical = 0
        prev_end = rectangles[0][2]
        for i in range(1, m):
            start, end = rectangles[i][0], rectangles[i][2]
            if prev_end <= start:
                vertical += 1
            prev_end = max(prev_end, end)

        rectangles.sort(key=lambda x: (x[1], x[3]))
        horizontal = 0
        prev_end = rectangles[0][3]
        for i in range(1, m):
            start, end = rectangles[i][1], rectangles[i][3]
            if prev_end <= start:
                horizontal += 1
            prev_end = max(prev_end, end)

        return vertical >= 2 or horizontal >= 2


s = Solution()
print(s.checkValidCuts(5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))
print(s.checkValidCuts(4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))
print(s.checkValidCuts(4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))
print(s.checkValidCuts(4, [[0, 0, 1, 4], [1, 0, 2, 3], [2, 0, 3, 3], [3, 0, 4, 3], [1, 3, 4, 4]]))
