from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency_list = [[] for _ in range(n)]
        for source, target, cost in flights:
            adjacency_list[source].append([target, cost])

        stops = {}
        pq = [[0, 0, src]]
        while pq:
            total, stops_so_far, node = heappop(pq)
            if node == dst:
                return total
            elif stops_so_far > k:
                continue
            elif node not in stops or stops_so_far < stops[node]:
                stops[node] = stops_so_far
                for neighbor, cost in adjacency_list[node]:
                    heappush(pq, [total + cost, stops_so_far + 1, neighbor])
        return -1


s = Solution()
print(s.findCheapestPrice(4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3,
                          k=1))
print(s.findCheapestPrice(3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
print(s.findCheapestPrice(3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
print(s.findCheapestPrice(5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2))
