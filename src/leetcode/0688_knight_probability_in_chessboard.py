from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        p = 1 / 8

        @cache
        def memo(curr_row, curr_col, moves):
            if not 0 <= curr_row < n or not 0 <= curr_col < n:
                return 0
            elif moves == 0:
                return 1
            ans = 0
            for dr, dc in directions:
                ans += memo(curr_row + dr, curr_col + dc, moves - 1)
            return ans * p

        return memo(row, column, k)


s = Solution()
print(s.knightProbability(n=3, k=2, row=0, column=0))
print(s.knightProbability(n=1, k=0, row=0, column=0))
