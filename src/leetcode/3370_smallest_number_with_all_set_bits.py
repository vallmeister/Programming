class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        while n > 0:
            n >>= 1
            ans <<= 1
            ans |= 1
        return ans


s = Solution()
print(s.smallestNumber(5))
print(s.smallestNumber(10))
print(s.smallestNumber(1))
print(s.smallestNumber(3))
