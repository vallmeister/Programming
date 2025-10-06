from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return

            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] == rank[ry]:
                parent[ry] = rx
                rank[rx] += 1

        def is_connected(x, y):
            return find(x) == find(y)

        connections.sort(key=lambda t: t[2])
        ans = 0
        for i, j, cost in connections:
            if is_connected(i, j):
                continue
            union(i, j)
            ans += cost
            n -= 1

        return ans if n == 1 else -1


s = Solution()
print(s.minimumCost(n=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
print(s.minimumCost(n=4, connections=[[1, 2, 3], [3, 4, 4]]))
