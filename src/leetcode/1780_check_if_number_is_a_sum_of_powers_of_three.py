class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = [1]
        while powers[-1] < n:
            powers.append(3 * powers[-1])
        while powers and n > 0:
            p = powers.pop()
            if p <= n:
                n -= p
        return n == 0


s = Solution()
print(s.checkPowersOfThree(12))
print(s.checkPowersOfThree(91))
print(s.checkPowersOfThree(21))
