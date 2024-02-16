class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parentheses_count = 0
        tmp = []
        for letter in s:
            if letter == '(':
                parentheses_count += 1
                tmp.append(letter)
            elif letter == ')':
                if parentheses_count > 0:
                    parentheses_count -= 1
                    tmp.append(letter)
            else:
                tmp.append(letter)
        ans = []
        for letter in reversed(tmp):
            if letter == '(' and parentheses_count > 0:
                parentheses_count -= 1
            else:
                ans.append(letter)
        return ''.join(reversed(ans))


sol = Solution()
print(sol.minRemoveToMakeValid("())()((("))
