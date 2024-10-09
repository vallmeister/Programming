class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        ans = 0
        for c in s:
            if c == '(':
                stack += 1
            elif c == ')':
                if stack <= 0:
                    ans += 1
                else:
                    stack -= 1
        return ans + stack
