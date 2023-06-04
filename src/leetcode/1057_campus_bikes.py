from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        all_pairs = []
        bike_available = [True] * m
        ans = [-1] * n
        for i in range(n):
            for j in range(m):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                all_pairs.append((distance, i, j))
        all_pairs.sort(reverse=True)
        while all_pairs:
            distance, worker, bike = all_pairs.pop()
            if ans[worker] != -1 or not bike_available[bike]:
                continue
            ans[worker] = bike
            bike_available[bike] = False
        return ans


s = Solution()
print(s.assignBikes([[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))
print(s.assignBikes([[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]))
