class Solution:
    # TODO: Fails with n=50
    def trailingZeroes(self, n: int) -> int:
        ans = 1
        num = 1
        for i in range(1, n + 1):
            num *= i
            if num % 10 ** ans == 0:
                ans += 1
            num %= 10 ** ans

        return ans - 1


s = Solution()
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
print(s.trailingZeroes(0))
print(s.trailingZeroes(10))
