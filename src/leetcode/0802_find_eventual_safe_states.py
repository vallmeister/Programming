from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        ascendants = [[] for _ in range(n)]
        safe_nodes = []
        candidates = deque()
        for i in range(n):
            if not graph[i]:
                candidates.append(i)
            for descendent in graph[i]:
                ascendants[descendent].append(i)

        while candidates:
            node = candidates.popleft()
            safe_nodes.append(node)
            for parent in ascendants[node]:
                graph[parent].remove(node)
                if not graph[parent]:
                    candidates.append(parent)

        safe_nodes.sort()
        return safe_nodes

    def dfs_solution(self, graph):
        n = len(graph)
        is_safe = [False] * n

        def dfs(node, visited):
            if is_safe[node]:
                return True
            elif node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor, visited):
                    return False
            is_safe[node] = True
            return True

        ans = []
        for i in range(n):
            if not graph[i]:
                is_safe[i] = True
                ans.append(i)
            elif dfs(i, set()):
                ans.append(i)
        return ans


s = Solution()
print(s.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))

print(s.dfs_solution([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(s.dfs_solution([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
