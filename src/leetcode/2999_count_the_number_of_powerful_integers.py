from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        @cache
        def memo(num, exponent):
            if num > finish:
                return 0
            ans = 0
            if start <= num <= finish:
                ans += 1
            for i in range(1, limit + 1):
                ans += memo(i * 10 ** exponent + num, exponent + 1)
            return ans

        return memo(int(s), len(s))


sol = Solution()
print(sol.numberOfPowerfulInt(start=1, finish=6000, limit=4, s="124"))
print(sol.numberOfPowerfulInt(start=15, finish=215, limit=6, s="10"))
print(sol.numberOfPowerfulInt(start=1000, finish=2000, limit=4, s="3000"))
print(sol.numberOfPowerfulInt(start=20, finish=1159, limit=5, s='20'))  # expected 8
