from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pass


s = Solution()
print(s.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
print(s.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
print(s.trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))
print(s.trapRainWater(
    [[78, 16, 94, 36], [87, 93, 50, 22], [63, 28, 91, 60], [64, 27, 41, 27], [73, 37, 12, 69], [68, 30, 83, 31],
     [63, 24, 68, 36]]))
