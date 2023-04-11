from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        neighbors = [[] for _ in range(n + 1)]
        for (u, v) in dislikes:
            neighbors[u].append(v)
            neighbors[v].append(u)
        group = [None] * (n + 1)
        group[1] = 0
        unassigned = deque([i for i in range(2, n + 1)])
        q = deque()
        q.append(1)
        while q or unassigned:
            if not q:
                next_node = unassigned.popleft()
                group[next_node] = 0
                q.append(next_node)
            node = q.popleft()
            for neighbor in neighbors[node]:
                if group[neighbor] == group[node]:
                    return False
                elif group[neighbor] is None:
                    group[neighbor] = 1 - group[node]
                    unassigned.remove(neighbor)
                    q.append(neighbor)
        return True


s = Solution()
print(s.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
print(s.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]))
print(s.possibleBipartition(10, [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]))
