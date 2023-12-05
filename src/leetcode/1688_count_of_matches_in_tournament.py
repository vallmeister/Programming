class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += (n - (n % 2)) // 2
            n = (n + (n % 2)) // 2
        return ans


s = Solution()
print(s.numberOfMatches(7))
print(s.numberOfMatches(14))
