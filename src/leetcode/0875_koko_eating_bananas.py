import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        while lower < upper:
            k = (lower + upper) // 2
            hours = self.hours_to_eat_piles(piles, k)

            if hours <= h:
                upper = k
            else:
                lower = k + 1
        return lower

    def hours_to_eat_piles(self, piles: list[int], k: int):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours


s = Solution()
print(s.minEatingSpeed([3, 6, 7, 11], 8))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
print(s.minEatingSpeed([312884470], 312884469))
