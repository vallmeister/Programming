from collections import deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_set = [set() for _ in range(n)]
        for u, v in edges:
            adjacency_set[u].add(v)
            adjacency_set[v].add(u)

        ans = 0
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            curr_component = []
            q = deque([i])
            while q:
                node = q.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                curr_component.append(node)
                for neighbor in adjacency_set[node]:
                    q.append(neighbor)
            if self.is_complete(curr_component, adjacency_set):
                ans += 1

        return ans

    def is_complete(self, component, adjacency_set):
        n = len(component)
        for i in range(n):
            u = component[i]
            for j in range(i + 1, n):
                v = component[j]
                if v not in adjacency_set[u]:
                    return False
        return True


s = Solution()
print(s.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
print(s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
