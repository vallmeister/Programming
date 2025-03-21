from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        def is_connected(x, y):
            return find(x) == find(y)

        cumulated_edge_weights = [2 ** 20 - 1] * n
        for u, v, weight in edges:
            cumulated_edge_weights[u] &= weight
            cumulated_edge_weights[v] &= weight
            union(u, v)
        components = [[] for _ in range(n)]
        for i in range(n):
            root = find(i)
            components[root].append(i)
        component_costs = {}
        for i, component in enumerate(components):
            cost = 2 ** 20 - 1
            for node in component:
                cost &= cumulated_edge_weights[node]
            component_costs[i] = cost

        ans = []
        for u, v in query:
            if is_connected(u, v):
                component = find(u)
                ans.append(component_costs[component])
            else:
                ans.append(-1)
        return ans


s = Solution()
print(s.minimumCost(n=5, edges=[[0, 1, 7], [1, 3, 7], [1, 2, 1]], query=[[0, 3], [3, 4]]))
print(s.minimumCost(n=3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]]))
