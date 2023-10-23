class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n >= 1:
            if n == 1:
                return True
            n /= 4.0
        return False


s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(1))
