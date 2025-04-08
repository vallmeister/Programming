from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        m = len(pizza)
        n = len(pizza[0])
        apples = self.get_apples(pizza)

        @cache
        def memo(row, col, cuts):
            if cuts == 0:
                if apples[row][col]:
                    return 1
                else:
                    return 0
            ans = 0
            piece = apples[row][col]
            for horizontal in range(row + 1, m):
                lower_piece = apples[horizontal][col]
                if piece == lower_piece or lower_piece == 0:
                    continue
                ans += memo(horizontal, col, cuts - 1)
                ans %= MOD

            for vertical in range(col + 1, n):
                right_piece = apples[row][vertical]
                if piece == right_piece or right_piece == 0:
                    continue
                ans += memo(row, vertical, cuts - 1)
                ans %= MOD
            return ans

        return memo(0, 0, k - 1)

    def get_apples(self, pizza):
        m = len(pizza)
        n = len(pizza[0])
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                apples[i][j] = apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
                if pizza[i][j] == 'A':
                    apples[i][j] += 1
        return apples

    def ways_bottom_up(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        apples = self.get_apples(pizza)
        mod = 10 ** 9 + 7

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if apples[i][j]:
                    dp[i][j][0] = 1

        for cuts in range(1, k):
            for i in reversed(range(m)):
                for j in reversed(range(n)):
                    piece = apples[i][j]

                    for horizontal in range(i + 1, m):
                        lower_piece = apples[horizontal][j]
                        if lower_piece in {0, piece}:
                            continue
                        dp[i][j][cuts] += dp[horizontal][j][cuts - 1]
                        dp[i][j][cuts] %= mod

                    for vertical in range(j + 1, n):
                        right_piece = apples[i][vertical]
                        if right_piece in {0, piece}:
                            continue
                        dp[i][j][cuts] += dp[i][vertical][cuts - 1]
                        dp[i][j][cuts] %= mod

        return dp[0][0][k - 1]


s = Solution()
print(s.ways(pizza=["A..", "AAA", "..."], k=3))
print(s.ways(pizza=["A..", "AA.", "..."], k=3))
print(s.ways(pizza=["A..", "A..", "..."], k=1))
print(s.ways(["...", "...", "..."], 1))
