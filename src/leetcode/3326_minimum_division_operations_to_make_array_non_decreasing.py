import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in reversed(range(n - 1)):
            if nums[i] <= nums[i + 1]:
                continue
            gpd = self.get_greatest_proper_divisor(nums[i])
            if nums[i] // gpd <= nums[i + 1]:
                nums[i] //= gpd
                ans += 1
            else:
                return -1

        return ans

    def get_greatest_proper_divisor(self, n):
        gpd = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                gpd = max(gpd, i, n // i)
        return gpd


s = Solution()
print(s.minOperations([25, 7]))
print(s.minOperations([5, 51, 25]))
print(s.minOperations([288, 7]))
