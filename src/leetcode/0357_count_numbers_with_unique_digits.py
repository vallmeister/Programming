import math
from functools import cache


class Solution:
    """
    Combinatorics
    """

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        return 9 * math.factorial(9) // math.factorial(10 - n) + self.countNumbersWithUniqueDigits(n - 1)

    """
    Digit DP
    """

    def count_nums_digit_dp(self, n) -> int:

        @cache
        def dp(i, mask, leading_zero):
            if i == n:
                return 1

            res = 0
            for digit in range(10):
                if leading_zero and digit == 0:
                    res += dp(i + 1, mask, True)
                else:
                    if mask & (1 << digit):
                        continue
                    res += dp(i + 1, mask | 1 << digit, False)
            return res

        return dp(0, 0, True)


s = Solution()
print(s.countNumbersWithUniqueDigits(1))
print(s.countNumbersWithUniqueDigits(2))
print(s.countNumbersWithUniqueDigits(0))
print(s.countNumbersWithUniqueDigits(3))
