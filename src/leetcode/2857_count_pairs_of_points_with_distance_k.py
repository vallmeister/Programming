from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        seen = defaultdict(int)
        ans = 0
        for x1, y1 in coordinates:
            for x in range(k + 1):
                y = k - x
                x2 = x ^ x1
                y2 = y ^ y1
                ans += seen[(x2, y2)]
            seen[(x1, y1)] += 1
        return ans


s = Solution()
print(s.countPairs(coordinates=[[1, 2], [4, 2], [1, 3], [5, 2]], k=5))
print(s.countPairs(coordinates=[[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], k=0))
print(s.countPairs(coordinates=[[1, 2], [4, 2], [1, 3], [5, 2], [6, 8]], k=5))
