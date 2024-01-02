from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m = len(workers)
        n = len(bikes)
        ans = 10 ** 9 + 4
        visited = [False] * n

        def backtracking(worker, curr_distance):
            nonlocal ans
            if worker == m:
                ans = min(ans, curr_distance)
                return
            elif curr_distance >= ans:
                return
            x0, y0 = workers[worker]
            for i in range(n):
                if visited[i]:
                    continue
                x1, y1 = bikes[i]
                visited[i] = True
                backtracking(worker + 1, curr_distance + abs(x1 - x0) + abs(y1 - y0))
                visited[i] = False

        backtracking(0, 0)
        return ans


s = Solution()
print(s.assignBikes([[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))
print(s.assignBikes([[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]))
print(s.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]], bikes=[[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]))
print(s.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
                    [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999], [6, 999], [7, 999], [8, 999],
                     [9, 999]]))
