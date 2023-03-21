class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1, 0]
        for j in range(1, n):
            new_row = [0] * (j + 1)
            for i in range(j, -1, -1):
                if i == j:
                    new_row[i] = 1
                elif s[i] == s[j]:
                    new_row[i] = 2 + dp[i + 1]
                else:
                    new_row[i] = max(new_row[i + 1], dp[i])
            dp = new_row
            dp.append(0)  # avoid index out of list for 2nd case
        return dp[0]

    def longest_palindrome_subseq_dp(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    def longest_palindrome_subseq_memo(self, s):
        memo = {}

        def longest_palindrome_subseq(i, j):
            if i > j:
                return 0
            elif (i, j) in memo:
                return memo[(i, j)]
            elif i == j:
                memo[(i, j)] = 1
                return memo[(i, j)]
            elif s[i] == s[j]:
                memo[(i, j)] = 2 + longest_palindrome_subseq(i + 1, j - 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(longest_palindrome_subseq(i + 1, j), longest_palindrome_subseq(i, j - 1))
                return memo[(i, j)]

        return longest_palindrome_subseq(0, len(s) - 1)


sol = Solution()
print(sol.longestPalindromeSubseq('bbbab'))
print(sol.longestPalindromeSubseq('cbbd'))
