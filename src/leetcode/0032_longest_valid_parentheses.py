class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n):
            if s[i - 1] == '(' and s[i] == ')':
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ')' and s[i] == ')':
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

        return max(dp)


sol = Solution()
print(sol.longestValidParentheses('(()'))
print(sol.longestValidParentheses(')()())'))
print(sol.longestValidParentheses(''))
print(sol.longestValidParentheses("(()))())("))
