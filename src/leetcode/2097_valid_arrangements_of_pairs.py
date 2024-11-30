from collections import deque, defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ans = []
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        graph = defaultdict(deque)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        def visit(node):
            while graph[node]:
                visit(graph[node].pop())
            ans.append(node)

        for node in out_degree.keys():
            if out_degree[node] == in_degree[node] + 1:
                start = node
                break
        else:
            start = pairs[0][0]

        visit(start)
        ans.reverse()
        return [[ans[i], ans[i + 1]] for i in range(len(pairs))]


sol = Solution()
print(sol.validArrangement([[17, 18], [18, 10], [10, 18]]))
