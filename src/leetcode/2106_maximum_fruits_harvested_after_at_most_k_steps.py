from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # note: it makes a difference whether you go first left then right or the other way round
        pass

s = Solution()
print(s.maxTotalFruits(fruits=[[2, 8], [6, 3], [8, 6]], startPos=5, k=4))
print(s.maxTotalFruits(fruits=[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos=5, k=4))
print(s.maxTotalFruits([[200000, 10000]], 200000, 200000))
print(s.maxTotalFruits([[0, 10000]], 200000, 200000))
print(s.maxTotalFruits(
    [[0, 7], [7, 4], [9, 10], [12, 6], [14, 8], [16, 5], [17, 8], [19, 4], [20, 1], [21, 3], [24, 3], [25, 3], [26, 1],
     [28, 10], [30, 9], [31, 6], [32, 1], [37, 5], [40, 9]], 21, 30))
