import math
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        upper = max(nums)
        lower = 1
        ans = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            if self.is_possible(nums, maxOperations, mid):
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return ans

    def is_possible(self, nums, operations, limit):
        for num in nums:
            if num <= limit:
                continue
            operations -= (math.ceil(num / limit) - 1)
        return operations >= 0


s = Solution()
print(s.minimumSize([9], 2))
print(s.minimumSize([2, 4, 8, 2], maxOperations=4))
