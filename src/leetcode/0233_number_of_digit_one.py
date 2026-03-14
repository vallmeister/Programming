from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        num = str(n)

        @cache
        def dp(i, ones, tight):
            if i == len(num):
                return ones

            limit = int(num[i])
            res = 0
            for digit in range(10):
                if digit > limit and tight:
                    continue
                res += dp(i + 1, ones + (1 if digit == 1 else 0), tight and digit == limit)
            return res

        return dp(0, 0, True)


s = Solution()
print(s.countDigitOne(13))
print(s.countDigitOne(0))
