class Solution:
    # TODO: find correct solution
    def removeSubstring(self, s: str, k: int) -> str:
        ans = []
        stack = []
        n = len(s)
        i = 0
        while i < n:
            opening = closing = 0
            while i < n and s[i] == '(':
                opening += 1
                i += 1
            while i < n and s[i] == ')':
                closing += 1
                i += 1
            while opening >= k and closing >= k:
                opening -= k
                closing -= k
            stack.append((opening, closing))

        prev_opening, prev_closing = stack[0]
        for curr_opening, curr_closing in stack[1:]:
            if prev_closing == 0 or curr_opening == 0:
                prev_opening += curr_opening
                prev_closing += curr_closing
            else:
                ans.append((prev_opening, prev_closing))
                prev_opening, prev_closing = curr_opening, curr_closing
            while prev_opening >= k and prev_closing >= k:
                prev_opening -= k
                prev_closing -= k
            if prev_opening == prev_closing == 0 and ans:
                prev_opening, prev_closing = ans.pop()
        ans.append((prev_opening, prev_closing))
        return ''.join('(' * opening + ')' * closing for opening, closing in ans)


sol = Solution()
print(sol.removeSubstring(s="(())", k=1))
print(sol.removeSubstring(s="(()(", k=1))
print(sol.removeSubstring(s="((()))()()()", k=3))
print(sol.removeSubstring("()())", 2))
print(sol.removeSubstring("(((())())(", 2))
print(sol.removeSubstring("()(((()((())())))())(((()()))(((()()()()()))()()))())())))(())",
                          2))  # "()(()())(((()()))(((()()()()()))()()))())())))"
