from collections import Counter
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        root = list(range(n))
        rank = [1] * n

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rank[rx] > rank[ry]:
                    root[ry] = rx
                elif rank[rx] < rank[ry]:
                    root[rx] = ry
                else:
                    root[ry] = rx
                    rank[rx] += 1

        for i in range(n):
            xi, yi = stones[i]
            for j in range(i + 1, n):
                xj, yj = stones[j]
                if xi == xj or yi == yj:
                    union(i, j)

        for i in range(n):
            find(i)

        return sum(v - 1 for v in Counter(root).values())


s = Solution()
print(s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(s.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(s.removeStones([[0, 0]]))
