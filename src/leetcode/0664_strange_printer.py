from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @cache
        def memo(i, j):
            if i > j:
                return 0
            ans = 1 + (memo(i + 1, j))
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    ans = min(ans, memo(i, k - 1) + memo(k + 1, j))
            return ans

        return memo(0, n - 1)


sol = Solution()
print(sol.strangePrinter("aaabbb"))
print(sol.strangePrinter("aba"))
print(sol.strangePrinter("ababc"))
