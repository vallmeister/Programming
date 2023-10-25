class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def recursive(n, k):
            if n == 0 and k == 0:
                return 0
            elif k % 2 == 0:
                return recursive(n - 1, k // 2)
            else:
                return 1 - recursive(n - 1, (k - 1) // 2)

        def iterative(n, k):
            bit = 0
            for _ in range(n):
                if k % 2 == 0:
                    k //= 2
                else:
                    bit = 1 - bit
                    k = (k - 1) // 2
            return bit

        return iterative(n - 1, k - 1)


s = Solution()
print(s.kthGrammar(1, 1))
print(s.kthGrammar(2, 1))
print(s.kthGrammar(2, 2))
