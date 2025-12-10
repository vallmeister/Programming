class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i ** 2 for i in range(1, n + 1)}
        ans = 0
        for aa in squares:
            for bb in squares:
                if aa + bb in squares:
                    ans += 1
        return ans


s = Solution()
print(s.countTriples(5))
print(s.countTriples(10))
