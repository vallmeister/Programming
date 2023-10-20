import math
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        nums.append(math.inf)
        curr_size = 0
        min_size = -math.inf

        for i in range(len(nums)):
            student = nums[i]
            if min_size < curr_size < student:
                ans += 1
            min_size = student
            curr_size += 1
        return ans


s = Solution()
print(s.countWays([1, 1]))
print(s.countWays([6, 0, 3, 3, 6, 7, 2, 7]))
