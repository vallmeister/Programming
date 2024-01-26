from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        MOD = 10 ** 9 + 7

        @cache
        def dfs(curr_row, curr_col, moves_left):
            if not 0 <= curr_row < m or not 0 <= curr_col < n:
                return 1
            elif moves_left <= 0:
                return 0
            result = 0
            for dr, dc in directions:
                result += dfs(curr_row + dr, curr_col + dc, moves_left - 1)
            return result

        return dfs(startRow, startColumn, maxMove) % MOD


s = Solution()
print(s.findPaths(2, 2, 2, 0, 0))
print(s.findPaths(1, 3, 3, 0, 1))
