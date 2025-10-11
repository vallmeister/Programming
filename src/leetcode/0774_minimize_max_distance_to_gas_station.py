import math
from typing import List


class Solution:

    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        EPSILON = 10 ** -6
        lower = EPSILON
        upper = 10 ** 8
        while upper - lower >= EPSILON:
            mid = (lower + upper) / 2
            if self.bin_search(stations, k, mid):
                upper = mid
            else:
                lower = mid + EPSILON

        return round(upper, 5)

    def bin_search(self, stations, k, target):
        n = len(stations)
        distances = []
        for i in range(1, n):
            s1 = stations[i - 1]
            s2 = stations[i]
            d = s2 - s1
            if d > target:
                distances.append(d)
        for d in distances:
            q = math.ceil(d / target) - 1
            k -= q
        return k >= 0


s = Solution()
print(s.minmaxGasDist(stations=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=9))
print(s.minmaxGasDist(stations=[23, 24, 36, 39, 46, 56, 57, 65, 84, 98], k=1))
print(s.minmaxGasDist([9, 34, 46, 51, 66, 81, 83, 84, 85, 91], 8))
