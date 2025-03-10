from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = [0] * (n * n + 1)
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                freq[num] += 1
        a = b = -1
        for i in range(1, n * n + 1):
            if freq[i] == 2:
                a = i
            elif freq[i] == 0:
                b = i
        return [a, b]
