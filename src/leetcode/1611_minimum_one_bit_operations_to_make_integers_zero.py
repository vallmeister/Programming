class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            k += 1
        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)


s = Solution()
print(s.minimumOneBitOperations(3))
print(s.minimumOneBitOperations(6))
print(s.minimumOneBitOperations(2))
print(s.minimumOneBitOperations(18))
print(s.minimumOneBitOperations(515264))
print(s.minimumOneBitOperations(862133))
