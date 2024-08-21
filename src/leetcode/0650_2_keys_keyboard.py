import math
from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:

        @cache
        def recursive(chars, buffer):
            if chars > n:
                return math.inf
            elif chars == n:
                return 0
            elif buffer == 0:
                return 2 + recursive(chars * 2, chars)
            return min(1 + recursive(chars + buffer, buffer), 2 + recursive(chars * 2, chars))

        return recursive(1, 0)


s = Solution()
print(s.minSteps(1))
print(s.minSteps(3))
