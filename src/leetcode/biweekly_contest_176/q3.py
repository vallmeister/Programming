from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)

        @cache
        def memo(i):
            if i >= n:
                return 0
            no_rob = memo(i + 1)
            yes_rob = nums[i] + (memo(i + 2) if i < n - 1 and colors[i] == colors[i + 1] else memo(i + 1))
            return max(yes_rob, no_rob)

        ans = memo(0)
        memo.cache_clear()
        return ans


s = Solution()
print(s.rob(nums=[1, 4, 3, 5], colors=[1, 1, 2, 2]))
