import math
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # monotonic stack
        stack = []
        low = -math.inf
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True


s = Solution()
print(s.verifyPreorder([5, 2, 1, 3, 6]))
print(s.verifyPreorder([5, 2, 6, 1, 3]))
