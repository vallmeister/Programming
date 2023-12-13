from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        total_visited = set()
        to_be_flipped = set()
        curr_visited = set()

        def dfs(i, j):
            curr_visited.add((i, j))
            ans = True
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                ans = False
            if i + 1 < m and board[i + 1][j] == 'O' and (i + 1, j) not in curr_visited:
                ans = dfs(i + 1, j) and ans
            if j + 1 < n and board[i][j + 1] == 'O' and (i, j + 1) not in curr_visited:
                ans = dfs(i, j + 1) and ans
            if i > 0 and board[i - 1][j] == 'O' and (i - 1, j) not in curr_visited:
                ans = dfs(i - 1, j) and ans
            if j > 0 and board[i][j - 1] == 'O' and (i, j - 1) not in curr_visited:
                ans = dfs(i, j - 1) and ans
            return ans

        for row in range(m):
            for col in range(n):
                curr_visited = set()
                if board[row][col] == 'O' and (row, col) not in total_visited:
                    if dfs(row, col):
                        to_be_flipped |= curr_visited
                    total_visited |= curr_visited
        for row, col in to_be_flipped:
            board[row][col] = 'X'


matrix = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
Solution().solve(matrix)
print(matrix)
