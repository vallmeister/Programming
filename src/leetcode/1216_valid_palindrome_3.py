from functools import cache


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        @cache
        def check_palindrome(i, j, removed):
            if removed > k:
                return False
            while i < j:
                if s[i] != s[j]:
                    return check_palindrome(i + 1, j, removed + 1) or check_palindrome(i, j - 1, removed + 1)
                i += 1
                j -= 1
            return True

        return check_palindrome(0, len(s) - 1, 0)

    def is_valid_palindrome_recursive(self, s, k):

        @cache
        def check_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return min(check_palindrome(i + 1, j), check_palindrome(i, j - 1)) + 1
                i += 1
                j -= 1
            return 0

        return check_palindrome(0, len(s) - 1) <= k

    def is_valid_palindrome_dp(self, s, k):
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n)[::-1]:
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1] <= k


sol = Solution()
print(sol.isValidPalindrome("abcdeca", k=2))
print(sol.isValidPalindrome("abbababa", k=1))
print(sol.is_valid_palindrome_recursive("abcdeca", k=2))
print(sol.is_valid_palindrome_recursive("abbababa", k=1))
print(sol.is_valid_palindrome_dp("abcdeca", k=2))
print(sol.is_valid_palindrome_dp("abbababa", k=1))
print(sol.is_valid_palindrome_dp("bacabaaa", 2))
