class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_so_far = 0
        n = len(s)
        i = 0
        while i < n:
            j = i
            stack = 0
            while j < n:
                if s[j] == '(':
                    stack += 1
                elif s[j] == ')':
                    stack -= 1
                if stack == 0:
                    longest_so_far = max(longest_so_far, j - i + 1)
                elif stack < 0:
                    break
                j += 1
            i = j + 1
        i = n - 1
        while i >= 0:
            j = i
            stack = 0
            while j >= 0:
                if s[j] == ')':
                    stack += 1
                elif s[j] == '(':
                    stack -= 1
                if stack == 0:
                    longest_so_far = max(longest_so_far, i - j + 1)
                elif stack < 0:
                    break
                j -= 1
            i = j - 1
        return longest_so_far


sol = Solution()
print(sol.longestValidParentheses('(()'))
print(sol.longestValidParentheses('")()())"'))
print(sol.longestValidParentheses(''))
