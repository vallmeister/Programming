from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        steps = 1

        def inside_grid(row, col):
            if 0 <= row < rows and 0 <= col < cols:
                ans.append([row, col])

        while len(ans) < rows * cols:
            # move east
            for _ in range(steps):
                cStart += 1
                inside_grid(rStart, cStart)

            # move south
            for _ in range(steps):
                rStart += 1
                inside_grid(rStart, cStart)

            steps += 1

            # move west
            for _ in range(steps):
                cStart -= 1
                inside_grid(rStart, cStart)

            # move north
            for _ in range(steps):
                rStart -= 1
                inside_grid(rStart, cStart)

            steps += 1
        return ans
