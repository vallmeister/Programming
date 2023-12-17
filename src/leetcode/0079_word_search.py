from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(row, col, idx):
            if idx >= len(word):
                return True
            letter = board[row][col]
            if letter == '#' or letter != word[idx]:
                return False
            board[row][col] = '#'
            tmp = False
            if row > 0:
                tmp = backtrack(row - 1, col, idx + 1) or tmp
            if col > 0:
                tmp = backtrack(row, col - 1, idx + 1) or tmp
            if row < m - 1:
                tmp = backtrack(row + 1, col, idx + 1) or tmp
            if col < n - 1:
                tmp = backtrack(row, col + 1, idx + 1) or tmp
            board[row][col] = letter
            return tmp

        for i in range(m):
            for j in range(n):
                if word == board[i][j] or word[0] == board[i][j] and backtrack(i, j, 0):
                    return True
        return False


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
print(s.exist([["a"]], 'a'))
