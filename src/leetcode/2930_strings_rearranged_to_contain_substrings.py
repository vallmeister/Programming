class Solution:
    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0
        MOD = 10 ** 9 + 7
        # all strings
        ans = 26 ** n

        # subtract strings with 0 Ls, 0 Ts, or <2 Es
        ans -= 3 * 25 ** n
        ans -= n * 25 ** (n - 1)

        # add strings with 0 Ls and 0Ts, 0 Ls and 0 Es, 0 Ls and 1 E, 1 E and 0 Ts, 0 Es and 0 Ts
        ans += 3 * 24 ** n
        ans += 2 * n * 24 ** (n - 1)

        # subtract strings with 0 Ls, 0 Ts and 0 or 1 Es
        ans -= 23 ** n
        ans -= n * 23 ** (n - 1)

        return ans % MOD


s = Solution()
print(s.stringCount(4))
print(s.stringCount(10))
print(s.stringCount(5))
print(s.stringCount(6))
