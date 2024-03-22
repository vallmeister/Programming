from functools import cache


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        MOD = 10 ** 9 + 7

        @cache
        def memo(i):
            if i >= n:
                return 1
            elif s[i] == '0':
                return 0
            ans = 0
            num = 0
            for j in range(i, n):
                num *= 10
                num += int(s[j])
                if num > k:
                    break
                ans += memo(j + 1)
                ans %= MOD
            return ans

        return memo(0)


sol = Solution()
print(sol.numberOfArrays('1000', 10000))
print(sol.numberOfArrays('1000', 10))
print(sol.numberOfArrays('1317', 2000))
