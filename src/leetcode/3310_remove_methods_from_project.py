from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = self.get_graph(n, invocations)
        suspicious = set()

        def dfs_suspicious(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for successor in g[node]:
                dfs_suspicious(successor)

        dfs_suspicious(k)
        visited = [False] * n

        def dfs(node):
            if node in suspicious:
                return False
            elif visited[node]:
                return True
            visited[node] = True
            res = True
            for successor in g[node]:
                res = res and dfs(successor)
            return res

        for i in range(n):
            if visited[i] or i in suspicious:
                continue
            elif not dfs(i):
                return list(range(n))

        return list(i for i in range(n) if i not in suspicious)

    def get_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        return graph


s = Solution()
print(s.remainingMethods(n=4, k=1, invocations=[[1, 2], [0, 1], [3, 2]]))
print(s.remainingMethods(n=5, k=0, invocations=[[1, 2], [0, 2], [0, 1], [3, 4]]))
print(s.remainingMethods(n=3, k=2, invocations=[[1, 2], [0, 1], [2, 0]]))
