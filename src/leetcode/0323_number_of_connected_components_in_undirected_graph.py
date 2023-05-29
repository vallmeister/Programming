from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))

        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)
            if parent_a == parent_b:
                return
            parents[parent_a] = parent_b

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        for u, v in edges:
            union(u, v)

        for i in range(n):
            find(i)

        return len(set(parents))


s = Solution()
print(s.countComponents(5, edges=[[0, 1], [1, 2], [3, 4]]))
print(s.countComponents(5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
