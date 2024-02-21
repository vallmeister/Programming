class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n


s = Solution()
print(s.isPowerOfTwo(-16))
print(s.isPowerOfTwo(-2147483648))
