import math
from heapq import heappop, heappush
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjacency_list = [[] for _ in range(n)]
        for source, target, cost in edges:
            self.adjacency_list[source].append((target, cost))

    def addEdge(self, edge: List[int]) -> None:
        source, target, cost = edge
        self.adjacency_list[source].append((target, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adjacency_list)
        pq = [(0, node1)]
        shortest_path = [math.inf] * n
        shortest_path[node1] = 0

        while pq:
            curr_cost, curr_node = heappop(pq)
            if curr_cost > shortest_path[curr_node]:
                continue
            if curr_node == node2:
                return curr_cost
            for neighbor, cost in self.adjacency_list[curr_node]:
                new_cost = curr_cost + cost
                if new_cost < shortest_path[neighbor]:
                    shortest_path[neighbor] = new_cost
                    heappush(pq, (new_cost, neighbor))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
