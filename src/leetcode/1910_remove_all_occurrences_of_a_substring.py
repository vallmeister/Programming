class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        def pattern_occurs():
            for i in range(1, m + 1):
                if stack[-i] != part[-i]:
                    return False
            return True

        for c in s:
            stack.append(c)
            if len(stack) >= m and pattern_occurs():
                for _ in range(m):
                    stack.pop()
        return ''.join(stack)


sol = Solution()
print(sol.removeOccurrences("daabcbaabcbc", 'abc'))
