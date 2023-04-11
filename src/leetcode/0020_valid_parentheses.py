class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in {'(', '{', '['}:
                stack.append(p)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening == '(' and p != ')':
                    return False
                elif opening == '[' and p != ']':
                    return False
                elif opening == '{' and p != '}':
                    return False
        return not bool(stack)


s = Solution()
print(s.isValid('()'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
