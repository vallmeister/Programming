from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        friends = set()
        friends_rows = []
        friends_cols = []
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    friends.add((row, col))
                    friends_rows.append(row)
        for col in range(n):
            for row in range(m):
                if grid[row][col] == 1:
                    friends_cols.append(col)
        median = len(friends) // 2
        meet_row, meet_col = friends_rows[median], friends_cols[median]
        distance = 0
        for row, col in friends:
            distance += abs(meet_row - row) + abs(meet_col - col)
        return distance


s = Solution()
print(s.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(s.minTotalDistance([[1, 1]]))
print(s.minTotalDistance(
    [[0, 1], [0, 1], [0, 1], [1, 1], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [0, 0], [0, 0],
     [1, 1], [0, 0]]))
print(s.minTotalDistance(
    [[1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0]]))
