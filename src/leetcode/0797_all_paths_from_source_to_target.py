import copy


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        paths = []

        def dfs(i, curr_path):
            if i == len(graph) - 1:
                paths.append(list(curr_path))
            else:
                for v in graph[i]:
                    curr_path.append(v)
                    dfs(v, curr_path)
                    curr_path.pop()

        dfs(0, [0])
        return paths


s = Solution()
print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [], [4], []]))
print(s.allPathsSourceTarget([[2], [], [1]]))
