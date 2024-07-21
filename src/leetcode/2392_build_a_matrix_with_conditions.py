from collections import deque
from typing import List


class Solution:
    def __topo_sort(self, n, edges):
        adj = [[] for _ in range(n + 1)]
        deg = [0] * (n + 1)
        order = []
        for u, v in edges:
            adj[u].append(v)
            deg[v] += 1
        q = deque()
        for i in range(1, n + 1):
            if deg[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            order.append(node)
            for desc in adj[node]:
                deg[desc] -= 1
                if deg[desc] == 0:
                    q.append(desc)
        if len(order) != n:
            return []
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order_rows = self.__topo_sort(k, rowConditions)
        order_cols = self.__topo_sort(k, colConditions)
        if not order_rows or not order_cols:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_cols[j]:
                    matrix[i][j] = order_rows[i]
                    break
        return matrix


s = Solution()
print(s.buildMatrix(k=3, rowConditions=[[1, 2], [3, 2]], colConditions=[[2, 1], [3, 2]]))
print(s.buildMatrix(k=3, rowConditions=[[1, 2], [2, 3], [3, 1], [2, 3]], colConditions=[[2, 1]]))
