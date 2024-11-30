from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls = set(tuple(w) for w in walls)
        guards = set(tuple(g) for g in guards)
        guarded = set()
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for gr, gc in guards:
            for dr, dc in directions:
                row = gr
                col = gc
                while True:
                    row += dr
                    col += dc
                    if row < 0 or row >= m or col < 0 or col >= n or (row, col) in walls or (row, col) in guards:
                        break
                    guarded.add((row, col))
        return m * n - len(guarded) - len(guards) - len(walls)


s = Solution()
print(s.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))
print(s.countUnguarded(2, 7, [[1, 5], [1, 1], [1, 6], [0, 2]], [[0, 6], [0, 3], [0, 5]]))
