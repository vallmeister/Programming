from functools import cache
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)

        @cache
        def memo(curr, f):
            if f < 0:
                return 0
            ans = 0
            if curr == finish:
                ans += 1
            for next_stop in range(n):
                if curr == next_stop:
                    continue
                ans += memo(next_stop, f - abs(locations[next_stop] - locations[curr]))
                ans %= MOD
            return ans

        return memo(start, fuel)

    def bottom_up(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10 ** 9 + 7
        dp = [[0] * (fuel + 1) for _ in range(n)]
        for f in range(fuel + 1):
            dp[finish][f] = 1
        for f in range(1, fuel + 1):
            for curr_city in range(n):
                for next_city in range(n):
                    distance = abs(locations[curr_city] - locations[next_city])
                    if curr_city == next_city or f < distance:
                        continue
                    dp[curr_city][f] += dp[next_city][f - distance]
                    dp[curr_city][f] %= MOD
        return dp[start][fuel]


s = Solution()
print(s.countRoutes(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))
print(s.countRoutes(locations=[4, 3, 1], start=1, finish=0, fuel=6))

print('\n', 10 * '-', 'Bottom-up DP', 10 * '-')
print(s.bottom_up(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))
print(s.bottom_up(locations=[4, 3, 1], start=1, finish=0, fuel=6))
print(s.bottom_up(locations=[5, 2, 1], start=0, finish=2, fuel=3))
