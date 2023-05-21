class Solution:
    # TODO: Revisit concept
    def parseTernary(self, expression: str) -> str:
        stack = []
        n = len(expression)
        for i in range(n - 1, -1, -2):
            if i == n - 1 or expression[i + 1] != '?':
                stack.append(expression[i])
                continue
            left = stack.pop()
            right = stack.pop()
            if expression[i] == 'T':
                stack.append(left)
            elif expression[i] == 'F':
                stack.append(right)
        return stack.pop()


s = Solution()
print(s.parseTernary('T?2:3'))
print(s.parseTernary('F?1:T?4:5'))
print(s.parseTernary('T?T?F:5:3'))
