from functools import cache
from typing import List


class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        if demand[0] > max(fuel):
            return -1

        n = len(demand)

        @cache
        def max_cars_to_serve(i, left, right):
            if i >= n:
                return 0
            curr_fuel = demand[i]
            take_left = take_right = 0
            if curr_fuel <= left:
                take_left = 1 + max_cars_to_serve(i + 1, left - curr_fuel, right)
            if curr_fuel <= right:
                take_right = 1 + max_cars_to_serve(i + 1, left, right - curr_fuel)
            return max(take_left, take_right)

        return max_cars_to_serve(0, fuel[0], fuel[1])


s = Solution()
print(s.minMaxWaitingTime(demand=[6, 8, 4, 6, 5], fuel=[16, 13]))
print(s.minMaxWaitingTime(demand=[10, 15], fuel=[12, 17]))
print(s.minMaxWaitingTime(demand=[10, 5], fuel=[8, 8]))
