from functools import cache


class Solution:
    def findIntegers(self, n: int) -> int:
        binary = self.get_binary(n)

        @cache
        def dp(i, is_prev_one, tight):
            if i == len(binary):
                return 1

            limit = int(binary[i])
            res = dp(i + 1, False, tight and limit == 0)

            if not is_prev_one and (not tight or tight and limit == 1):
                res += dp(i + 1, True, tight and limit == 1)
            return res

        return dp(0, False, True)

    def get_binary(self, n):
        digits = []
        while n > 0:
            digits.append(str(n % 2))
            n //= 2
        return ''.join(reversed(digits))


s = Solution()
print(s.findIntegers(5))
print(s.findIntegers(1))
print(s.findIntegers(2))
print(s.findIntegers(16))
