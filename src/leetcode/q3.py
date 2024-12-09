from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n_left = len(edges1) + 1
        n_right = len(edges2) + 1

        g_left = [[] for _ in range(n_left)]
        for u, v in edges1:
            g_left[u].append(v)
            g_left[v].append(u)

        g_right = [[] for _ in range(n_right)]
        for u, v in edges2:
            g_right[u].append(v)
            g_right[v].append(u)

        reachable_left = [self.bfs(g_left, i, k) for i in range(n_left)]
        reachable_right = [self.bfs(g_right, i, k - 1) for i in range(n_right)]
        ans = []
        mx = max(reachable_right)
        for i in range(n_left):
            ans.append(mx + reachable_left[i])
        return ans

    def bfs(self, graph, start, k):
        ans = 0
        visited = set()
        q = [(start, 0)]
        while q:
            next_q = []
            for node, d in q:
                if node in visited or d > k:
                    continue
                visited.add(node)
                ans += 1
                for neighbor in graph[node]:
                    next_q.append((neighbor, d + 1))
            q = next_q
        return ans


s = Solution()
print(s.maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                       edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], k=2))
