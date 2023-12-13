from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        variables = set()
        for i in range(len(equations)):
            nominator, denominator = equations[i]
            graph[nominator][denominator] = values[i]
            graph[denominator][nominator] = 1 / values[i]
            variables.add(nominator)
            variables.add(denominator)
        ans = [-1.0] * len(queries)

        def dfs(var, target, idx, curr, visited):
            if var not in variables or var in visited:
                return
            visited.add(var)
            if var == target:
                ans[idx] = curr
            for neighbor, cost in graph[var].items():
                dfs(neighbor, target, idx, curr * cost, visited)

        for i in range(len(queries)):
            start, end = queries[i]
            dfs(start, end, i, 1.0, set())
        return ans


s = Solution()
print(s.calcEquation([["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                     queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print(s.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                     queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
print(s.calcEquation([["a", "b"]], values=[0.5], queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
