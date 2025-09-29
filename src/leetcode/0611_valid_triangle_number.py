import bisect
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                k = bisect.bisect_right(nums, nums[i] + nums[j] - 1)
                ans += max(0, k - j - 1)
        return ans


s = Solution()
print(s.triangleNumber([2, 2, 3, 4]))
print(s.triangleNumber([4, 2, 3, 4]))
print(s.triangleNumber([0, 0]))
