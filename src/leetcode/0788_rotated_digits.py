from functools import cache


class Solution:
    """
    Brute force
    """

    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            is_different = False
            while i > 0:
                digit = i % 10
                if digit in {3, 4, 7}:
                    break
                is_different |= (digit in {2, 5, 6, 9})
                i //= 10
            else:
                ans += (1 if is_different else 0)
        return ans

    """
    Digit DP
    """

    def rotated_digits(self, n) -> int:
        same_digits = {0, 1, 8}
        different_digits = {2, 5, 6, 9}
        num = str(n)

        @cache
        def digit_dp(i, is_tight, is_different):
            if i >= len(num):
                return 1 if is_different else 0
            limit = int(num[i])
            ans = 0
            for j in same_digits | different_digits:
                if is_tight and j > limit:
                    continue
                ans += digit_dp(i + 1, is_tight and limit == j, is_different or j in different_digits)
            return ans

        return digit_dp(0, True, False)


s = Solution()
print(s.rotatedDigits(10))
print(s.rotatedDigits(1))
print(s.rotatedDigits(2))

print(s.rotated_digits(10))
print(s.rotated_digits(1))
print(s.rotated_digits(2))
