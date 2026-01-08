from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = self.get_graph(n, edges)
        ans = [0] * n

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            total = 0
            for child, d in g[node]:
                if not visited[child]:
                    total += d + dfs(child)
            return total

        ans[0] = dfs(0)
        visited = [False] * n

        def dfs_dp(node):
            visited[node] = True
            for child, d in g[node]:
                if visited[child]:
                    continue
                ans[child] = ans[node]
                ans[child] += (-2 * d + 1)
                dfs_dp(child)

        dfs_dp(0)
        return ans

    def get_graph(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append([v, 0])
            g[v].append([u, 1])
        return g


s = Solution()
print(s.minEdgeReversals(n=4, edges=[[2, 0], [2, 1], [1, 3]]))
print(s.minEdgeReversals(n=3, edges=[[1, 2], [2, 0]]))
