class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = [i for i in range(n)]

        def union(u, v):
            u_parent = find(u)
            v_parent = find(v)
            if u_parent != v_parent:
                parent[u_parent] = v_parent

        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]

        for u, v in connections:
            union(u, v)

        representatives = set()
        for i in range(n):
            representatives.add(find(i))
        return len(representatives) - 1


s = Solution()
print(s.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))
print(s.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
print(s.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))
