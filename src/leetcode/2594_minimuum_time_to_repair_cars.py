import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = ans = cars ** 2 * 100
        while left <= right:
            mid = (left + right) // 2
            if self.check_time(ranks, cars, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def check_time(self, ranks, cars, time):
        for rank in ranks:
            cars -= math.floor(math.sqrt(time / rank))
        return cars <= 0


s = Solution()
print(s.repairCars([4, 3, 2, 1], 10))
print(s.repairCars([5, 1, 8], 6))
