from functools import cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        number = str(n)
        digits = digits

        @cache
        def digit_dp(i, tight, leading_zeroes):
            if i >= len(number):
                return 0 if leading_zeroes else 1
            limit = number[i]
            ans = (digit_dp(i + 1, tight and limit == '0', leading_zeroes) if leading_zeroes else 0)
            for d in digits:
                if tight and d > limit:
                    continue
                ans += digit_dp(i + 1, tight and d == limit, leading_zeroes and d == '0')
            return ans

        return digit_dp(0, True, True)


s = Solution()
print(s.atMostNGivenDigitSet(digits=["1", "3", "5", "7"], n=100))
print(s.atMostNGivenDigitSet(digits=["1", "4", "9"], n=1000000000))
print(s.atMostNGivenDigitSet(digits=["7"], n=8))
