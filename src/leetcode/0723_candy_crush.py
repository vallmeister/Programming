class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        m = len(board)
        n = len(board[0])

        def find_and_crush():
            candidates = set()
            for i in range(m):
                start = end = 0
                while end < n:
                    cache = set()
                    while end < n and board[i][end] != 0 and board[i][start] == board[i][end]:
                        cache.add((i, end))
                        end += 1
                    if len(cache) >= 3:
                        candidates = candidates.union(cache)
                    if start == end:
                        end += 1
                    start = end
            for i in range(n):
                start = end = 0
                while end < m:
                    cache = set()
                    while end < m and board[end][i] != 0 and board[start][i] == board[end][i]:
                        cache.add((end, i))
                        end += 1
                    if len(cache) >= 3:
                        candidates = candidates.union(cache)
                    if start == end:
                        end += 1
                    start = end
            for i, j in candidates:
                board[i][j] = 0
            return len(candidates)

        def drop_and_fill():
            pass

        while find_and_crush():
            drop_and_fill()
        return board


s = Solution()
print(s.candyCrush([[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
                    [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
                    [4, 1, 4, 4, 1014]]))
print(s.candyCrush([[1, 3, 5, 5, 2], [3, 4, 3, 3, 1], [3, 2, 4, 5, 2], [2, 4, 4, 5, 5], [1, 4, 4, 1, 1]]))
