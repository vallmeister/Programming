from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        EPSILON = 10 ** (-5)
        lower = upper = 0
        for _, y, l in squares:
            upper = max(upper, y + l)

        while lower + EPSILON <= upper:
            mid = round((lower + upper) / 2, 6)
            diff = self.get_difference(squares, mid)
            if diff > EPSILON:
                lower = mid
            else:
                upper = mid
        return lower

    def get_difference(self, squares, cut):
        square_sum = 0
        for _, y, l in squares:
            area = l * l
            if y + l <= cut:
                square_sum -= area
            elif y >= cut:
                square_sum += area
            else:
                b = (y + l - cut) / l
                square_sum += b * area - (1 - b) * area
        return square_sum


s = Solution()
print(s.separateSquares([[0, 0, 1], [2, 2, 1]]))
print(s.separateSquares([[0, 0, 2], [1, 1, 1]]))
