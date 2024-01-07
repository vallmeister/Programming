import math
from functools import cache


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:

        @cache
        def recursive(number):
            if number <= y:
                return y - number
            elif number < 0 or number > 11 * x:
                return math.inf
            r_5 = number % 5
            r_11 = number % 11
            return min(r_5 + 1 + recursive(number // 5), r_11 + 1 + recursive(number // 11),
                       5 - r_5 + 1 + recursive(number // 5 + 1), 11 - r_11 + 1 + recursive(number // 11 + 1),
                       number - y)

        return recursive(x)


s = Solution()
print(s.minimumOperationsToMakeEqual(26, 1))
print(s.minimumOperationsToMakeEqual(54, 2))
print(s.minimumOperationsToMakeEqual(25, 30))
print(s.minimumOperationsToMakeEqual(2, 1))
print(s.minimumOperationsToMakeEqual(14, 2))
