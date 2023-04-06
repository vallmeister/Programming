class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe_nodes = [None] * n

        def dfs(node, visited):
            if safe_nodes[node] is not None:
                return safe_nodes[node]
            elif not graph[node]:
                safe_nodes[node] = True
                return safe_nodes[node]
            tmp = True
            for child in graph[node]:
                if child in visited:
                    safe_nodes[node] = False
                    return safe_nodes[node]
                else:
                    visited.add(node)
                    tmp = dfs(child, visited) and tmp
                    visited.remove(node)
            safe_nodes[node] = tmp
            return tmp

        for i in range(n):
            if safe_nodes[i] is None:
                dfs(i, set())
        return [i for i in range(n) if safe_nodes[i]]


s = Solution()
print(s.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
