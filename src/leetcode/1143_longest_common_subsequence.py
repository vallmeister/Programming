class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [0] * (n+1)
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (n+1)
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    new_dp[j] = 1 + dp[j + 1]
                else:
                    new_dp[j] = max(new_dp[j + 1], dp[j])
            dp = new_dp
        return dp[0]

    def longest_common_subsequence_dp(self, text1, text2):
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]

    def longest_common_subsequence_memo(self, text1, text2):
        memo = {}

        def longest_common_subsequence(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif (i, j) in memo:
                return memo[(i, j)]
            elif text1[i] == text2[j]:
                memo[(i, j)] = 1 + longest_common_subsequence(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(longest_common_subsequence(i + 1, j), longest_common_subsequence(i, j + 1))
                return memo[(i, j)]

        return longest_common_subsequence(0, 0)


s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
print(s.longestCommonSubsequence('abc', 'abc'))
print(s.longestCommonSubsequence('abc', 'def'))
print(s.longestCommonSubsequence('bl', 'yby'))
