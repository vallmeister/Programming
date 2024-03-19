from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def memo(top, bot):
            if top < 0 or bot < 0:
                return 0
            elif top == 0 == bot:
                return 1
            ans = 0
            # domino tile horizontally
            if top >= bot:
                ans += memo(top - 2, bot)
            else:
                ans += memo(top, bot - 2)
            if top == bot:
                ans += memo(top - 1, bot - 1)  # domino tile vertically
                ans += memo(top - 2, bot - 1)  # tromino tile p
                ans += memo(top - 1, bot - 2)  # tromino tile l
            elif bot - 1 == top:
                ans += memo(top - 1, bot - 2)  # tromino tile mirrored l
            elif top - 1 == bot:
                ans += memo(top - 2, bot - 1)  # tromino tile q
            return ans % MOD

        return memo(n, n)


s = Solution()
print(s.numTilings(3))
print(s.numTilings(2))
print(s.numTilings(1))
