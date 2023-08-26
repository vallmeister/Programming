from collections import deque


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = True
        for i in range(n + 1):
            dp[i][0] = True



s = Solution()
print(s.isInterleave("aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.isInterleave("aabcc", s2="dbbca", s3="aadbbbaccc"))
print(s.isInterleave('', '', ''))
