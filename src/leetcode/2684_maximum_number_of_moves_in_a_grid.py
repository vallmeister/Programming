from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        curr_col = [0] * m
        curr_move = [True] * m
        ans = 0
        for j in range(n - 1):
            next_col = [0] * m
            next_move = [False] * m
            for i in range(m):
                if not curr_move[i]:
                    continue
                if i > 0 and grid[i][j] < grid[i - 1][j + 1]:
                    next_col[i - 1] = max(next_col[i - 1], curr_col[i] + 1)
                    next_move[i - 1] = True
                if grid[i][j] < grid[i][j + 1]:
                    next_col[i] = max(next_col[i], curr_col[i] + 1)
                    next_move[i] = True
                if i < m - 1 and grid[i][j] < grid[i + 1][j + 1]:
                    next_col[i + 1] = max(next_col[i + 1], curr_col[i] + 1)
                    next_move[i + 1] = True
            curr_col = next_col
            ans = max(ans, max(curr_col))
            curr_move = next_move
        return ans


s = Solution()
print(s.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))
print(s.maxMoves([[187, 167, 209, 251, 152, 236, 263, 128, 135], [267, 249, 251, 285, 73, 204, 70, 207, 74],
                  [189, 159, 235, 66, 84, 89, 153, 111, 189], [120, 81, 210, 7, 2, 231, 92, 128, 218],
                  [193, 131, 244, 293, 284, 175, 226, 205, 245]]))
