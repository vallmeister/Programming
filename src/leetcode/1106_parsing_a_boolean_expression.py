class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ',':
                continue
            elif char == ')':
                literals = set()
                while stack[-1] != '(':
                    literals.add(stack.pop())
                stack.pop()
                op = stack.pop()
                if op == '!':
                    stack.append('t' if not literals.pop() == 't' else 'f')
                elif op == '&':
                    stack.append('t' if 'f' not in literals else 'f')
                elif op == '|':
                    stack.append('t' if 't' in literals else 'f')
            else:
                stack.append(char)
        return 't' == stack[0]


s = Solution()
print(s.parseBoolExpr("&(|(f))"))
print(s.parseBoolExpr("|(f,f,f,t)"))
print(s.parseBoolExpr("!(&(f,t))"))
