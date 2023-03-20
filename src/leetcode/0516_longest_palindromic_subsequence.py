class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longest_palindrome_subseq_dp(s)

    def longest_palindrome_subseq_dp(self, s):
        n = len(s)
        if s == s[::-1]:
            return n
        dp = [[0] * 2 for _ in range(n + 1)]
        
        print(dp)
        return max(dp[0])

    def longest_palindrome_subseq_memo(self, s):
        memo = {}

        def longest_palindrome_subseq(s1, i):
            n = len(s1)
            if s1 == s1[::-1]:
                return n
            elif (s1, i) in memo:
                return memo[(s1, i)]
            elif i >= n:
                memo[(s1, i)] = 0
                return memo[(s1, i)]
            else:
                memo[(s1, i)] = max(longest_palindrome_subseq(s1, i + 1),
                                    longest_palindrome_subseq(s1[:i] + s1[i + 1:], i))
                return memo[(s1, i)]

        return longest_palindrome_subseq(s, 0)


sol = Solution()
print(sol.longestPalindromeSubseq('bbbab'))
print(sol.longestPalindromeSubseq('cbbd'))
