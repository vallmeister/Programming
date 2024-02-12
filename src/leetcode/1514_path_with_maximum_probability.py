import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        adjacency_list = [[] for _ in range(n)]
        for i in range(len(edges)):
            source, target = edges[i]
            p = succProb[i]
            adjacency_list[source].append([target, 1 / p])
            adjacency_list[target].append([source, 1 / p])

        paths = [math.inf] * n
        pq = [(1, start_node)]
        while pq:
            curr_dis, node = heappop(pq)
            if curr_dis < paths[node]:
                paths[node] = curr_dis
                for neighbor, p in adjacency_list[node]:
                    heappush(pq, (p * curr_dis, neighbor))
        return 1 / paths[end_node]


s = Solution()
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print(s.maxProbability(3, [[0, 1]], [0.5], 0, 2))
