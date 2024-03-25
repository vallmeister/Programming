from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def memo(i):
            if i >= n:
                return 1
            elif s[i] == '0':
                return 0
            elif i == n - 1 and s[i] == '*':
                return 9
            elif i == n - 1:
                return 1
            elif s[i] != '*' and s[i + 1] != '*' and 1 <= int(s[i:i+2]) <= 26:
                return memo(i + 2) + memo(i + 1)
            pass


sol = Solution()
print(sol.numDecodings('*'))
print(sol.numDecodings('1*'))
print(sol.numDecodings('2*'))
