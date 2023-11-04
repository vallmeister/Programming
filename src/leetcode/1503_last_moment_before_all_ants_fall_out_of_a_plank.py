from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left and right:
            return max(max(left), n - min(right))
        elif left:
            return max(left)
        else:
            return n - min(right)


s = Solution()
print(s.getLastMoment(4, left=[4, 3], right=[0, 1]))
print(s.getLastMoment(7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]))
print(s.getLastMoment(7, left=[0, 1, 2, 3, 4, 5, 6, 7], right=[]))
