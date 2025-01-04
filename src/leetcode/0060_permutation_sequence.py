import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.recursion(n, k - 1, list(range(1, n + 1)))

    def recursion(self, n, k, digits):
        if len(digits) == 1:
            return str(digits[0])
        n_fac = math.factorial(n)
        bucket_size = n_fac // len(digits)
        idx = k // bucket_size
        return str(digits.pop(idx)) + self.recursion(n - 1, k - idx * bucket_size, digits)


s = Solution()
print(s.getPermutation(3, 3))
