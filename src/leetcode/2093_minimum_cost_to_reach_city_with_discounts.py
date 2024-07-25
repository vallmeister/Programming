import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adjacency = [[] for _ in range(n)]
        for u, v, toll in highways:
            adjacency[u].append((v, toll))
            adjacency[v].append((u, toll))

        distances = [[math.inf] * (discounts + 1) for _ in range(n)]
        distances[0][0] = 0
        visited = [[False] * (discounts + 1) for _ in range(n)]

        pq = [(0, 0, 0)]
        while pq:
            current_costs, city, discounts_used = heappop(pq)
            if visited[city][discounts_used]:
                continue
            visited[city][discounts_used] = True
            for neighbor, toll in adjacency[city]:

                if current_costs + toll < distances[neighbor][discounts_used]:
                    distances[neighbor][discounts_used] = current_costs + toll
                heappush(pq, (current_costs + toll, neighbor, discounts_used))

                if discounts_used < discounts and current_costs + toll // 2 < distances[neighbor][discounts_used + 1]:
                    distances[neighbor][discounts_used + 1] = current_costs + toll // 2
                    heappush(pq, (current_costs + toll // 2, neighbor, discounts_used + 1))
        min_cost = min(distances[n - 1])
        return min_cost if min_cost < math.inf else -1


s = Solution()
print(s.minimumCost(5, highways=[[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]], discounts=1))
print(s.minimumCost(n=4, highways=[[1, 3, 17], [1, 2, 7], [3, 2, 5], [0, 1, 6], [3, 0, 20]], discounts=20))
print(s.minimumCost(n=4, highways=[[0, 1, 3], [2, 3, 2]], discounts=0))
