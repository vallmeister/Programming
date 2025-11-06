from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = self.get_graph(c, connections)
        power_grids = [[]]
        station_grids = [-1] * (c + 1)
        curr_grid = 0
        for i in range(1, c + 1):
            if station_grids[i] > -1:
                continue
            self.bfs(g, i, station_grids, power_grids, curr_grid)
            curr_grid += 1
            power_grids.append([])
        is_online = [True] * (c + 1)
        ans = []
        for request, station in queries:
            match request:
                case 1:
                    if is_online[station]:
                        ans.append(station)
                    else:
                        grid = station_grids[station]
                        while power_grids[grid] and not is_online[power_grids[grid][0]]:
                            heappop(power_grids[grid])
                        if power_grids[grid]:
                            ans.append(power_grids[grid][0])
                        else:
                            ans.append(-1)
                case 2:
                    is_online[station] = False
        return ans

    def get_graph(self, n, edges):
        # 1-indexed
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g

    def bfs(self, graph, start, station_grids, power_grids, grid):
        q = deque([start])
        while q:
            station = q.popleft()
            if station_grids[station] > -1:
                continue
            station_grids[station] = grid
            heappush(power_grids[grid], station)
            for neighbor in graph[station]:
                q.append(neighbor)


s = Solution()
print(s.processQueries(c=5, connections=[[1, 2], [2, 3], [3, 4], [4, 5]],
                       queries=[[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]))
print(s.processQueries(c=3, connections=[], queries=[[1, 1], [2, 1], [1, 1]]))
