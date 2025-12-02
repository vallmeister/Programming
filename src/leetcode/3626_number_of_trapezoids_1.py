from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        hpoints = defaultdict(int)
        hpairs = defaultdict(int)
        total_pairs = ans = 0
        for _, y in points:
            num_points = hpoints[y]
            ans += num_points * (max(total_pairs - num_points * (num_points - 1) // 2, 0))
            ans %= MOD
            total_pairs += num_points
            hpairs[y] += num_points
            hpoints[y] += 1
        return ans


s = Solution()
print(s.countTrapezoids(points=[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(s.countTrapezoids(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))
