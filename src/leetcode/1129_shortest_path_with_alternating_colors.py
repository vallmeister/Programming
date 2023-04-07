from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        red_neighbors = [[] for _ in range(n)]
        blue_neighbors = [[] for _ in range(n)]
        for u, v in redEdges:
            red_neighbors[u].append(v)
        for u, v in blueEdges:
            blue_neighbors[u].append(v)
        visited = [[False, False, False] for _ in range(n)]
        visited[0] = [True, True, False]
        paths = [-1] * n
        paths[0] = 0
        q = deque()
        q.append((0, 0, 2))
        while q:
            node, distance, color = q.popleft()  # color: 0 indicates red, 1 indicates blue
            if color != 0:
                for neighbor in red_neighbors[node]:
                    if not visited[neighbor][0]:
                        if paths[neighbor] == -1:
                            paths[neighbor] = distance + 1
                        visited[neighbor][0] = True
                        q.append((neighbor, distance + 1, 0))
            if color != 1:
                for neighbor in blue_neighbors[node]:
                    if not visited[neighbor][1]:
                        if paths[neighbor] == -1:
                            paths[neighbor] = distance + 1
                        visited[neighbor][1] = True
                        q.append((neighbor, distance + 1, 1))

        return paths


s = Solution()
print(s.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []))
print(s.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]))
print(s.shortestAlternatingPaths(3, [[0, 1], [0, 2]], [[1, 0]]))
print(s.shortestAlternatingPaths(5, [[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [2, 1], [2, 0], [1, 4], [3, 4]],
                                 [[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]))
