class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            curr = s[i]
            if stack and abs(ord(curr) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr)
        return ''.join(stack)
