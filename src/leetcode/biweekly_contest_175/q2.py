import math
from typing import List


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        lower = 1
        upper = ans = 10 ** 5
        while lower <= upper:
            k = (lower + upper) // 2
            if self.non_positive(nums, k):
                ans = k
                upper = k - 1
            else:
                lower = k + 1
        return ans

    def non_positive(self, nums, k):
        num_operations = 0
        for num in nums:
            num_operations += math.ceil(num / k)
        return num_operations <= k * k
