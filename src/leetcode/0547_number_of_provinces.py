class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
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

        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    union(i, j)

        representatives = set()
        for i in range(n):
            representatives.add(find(i))
        return len(representatives)


s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
