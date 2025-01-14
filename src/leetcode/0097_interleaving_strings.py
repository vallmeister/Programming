from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        p = len(s3)

        if m + n != p:
            return False

        @cache
        def memo(i, j, k):
            if i >= m and j >= n and k >= p:
                return True
            fst = snd = False
            if i < m and s1[i] == s3[k]:
                fst = memo(i + 1, j, k + 1)
            if j < n and s2[j] == s3[k]:
                snd = memo(i, j + 1, k + 1)
            return fst or snd

        return memo(0, 0, 0)

    def dynamic_programming(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        p = len(s3)

        if m + n != p:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m + 1)):
            for j in reversed(range(n + 1)):
                if i == m and j == n:
                    dp[i][j] = True
                elif i == m:
                    dp[i][j] = s2[j] == s3[i + j] and dp[i][j + 1]
                elif j == n:
                    dp[i][j] = s1[i] == s3[i + j] and dp[i + 1][j]
                else:
                    dp[i][j] = s1[i] == s3[i + j] and dp[i + 1][j] or s2[j] == s3[i + j] and dp[i][j + 1]
        return dp[0][0]


s = Solution()
print('-' * 10, 'memoization', '-' * 10)
print(s.isInterleave("aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.isInterleave("aabcc", s2="dbbca", s3="aadbbbaccc"))
print(s.isInterleave('', '', ''))

print('-' * 10, 'dp', '-' * 10)

print(s.dynamic_programming("aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.dynamic_programming("aabcc", s2="dbbca", s3="aadbbbaccc"))
print(s.dynamic_programming('', '', ''))
