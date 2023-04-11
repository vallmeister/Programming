from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                q = deque()
                q.append(i)
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if colors[neighbor] == colors[node]:
                            return False
                        elif colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[node]
                            q.append(neighbor)
        return True


s = Solution()
print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
