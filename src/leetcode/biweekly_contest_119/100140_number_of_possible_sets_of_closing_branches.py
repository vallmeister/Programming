import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0
        adjacency_matrix = [[math.inf] * n for _ in range(n)]
        for u, v, weight in roads:
            adjacency_matrix[u][v] = min(adjacency_matrix[u][v], weight)
            adjacency_matrix[v][u] = min(adjacency_matrix[v][u], weight)

        power_set = []

        def sub_set(curr_list, last_element):
            power_set.append(list(curr_list))
            for i in range(last_element, n):
                curr_list.append(i)
                sub_set(curr_list, i + 1)
                curr_list.pop()

        def dijkstra(node, active_branches):
            curr_distances = {i: math.inf for i in active_branches}
            curr_distances[node] = 0
            q = [(0.0, node)]
            while q:
                distance, curr_node = heappop(q)
                for neighbor in active_branches:
                    curr_distance = adjacency_matrix[curr_node][neighbor]
                    if curr_distance + distance < curr_distances[neighbor]:
                        curr_distances[neighbor] = curr_distance + distance
                        heappush(q, (curr_distance + distance, neighbor))
            return curr_distances

        sub_set([], 0)
        for branches in power_set:
            if not branches:
                ans += 1
                continue
            for start in branches:
                distances = dijkstra(start, branches)
                if maxDistance < max(distances.values()):
                    break
            else:
                ans += 1
        return ans


s = Solution()
print(s.numberOfSets(3, maxDistance=5, roads=[[0, 1, 2], [1, 2, 10], [0, 2, 10]]))
print(s.numberOfSets(n=3, maxDistance=5, roads=[[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]))
print(s.numberOfSets(n=1, maxDistance=10, roads=[]))
