from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for chisato in range(n):
            for takina in range(n):
                if chisato == takina:
                    continue
                x0, y0 = points[chisato]
                x1, y1 = points[takina]
                if x1 < x0 or y1 > y0:
                    continue
                for person in range(n):
                    if person == chisato or person == takina:
                        continue
                    x2, y2 = points[person]
                    if x0 <= x2 <= x1 and y1 <= y2 <= y0:
                        break
                else:
                    ans += 1
        return ans


s = Solution()
print(s.numberOfPairs([[1, 1], [2, 2], [3, 3]]))
print(s.numberOfPairs([[6, 2], [4, 4], [2, 6]]))
print(s.numberOfPairs([[3, 1], [1, 3], [1, 1]]))
print(s.numberOfPairs([[0, 0], [0, 3]]))
print(s.numberOfPairs([[0, 0], [0, 6], [0, 3], [1, 0]]))
