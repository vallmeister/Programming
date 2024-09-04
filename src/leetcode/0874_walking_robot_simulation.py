import itertools
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cd = 0
        x = y = 0
        obstacles = set(tuple(o) for o in obstacles)
        max_dist = 0
        for c in commands:
            if c == -2:
                cd += 4
                cd -= 1
                cd %= 4
            elif c == -1:
                cd += 1
                cd %= 4
            else:
                dx, dy = directions[cd]
                for _ in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x ** 2 + y ** 2)
        return max_dist
