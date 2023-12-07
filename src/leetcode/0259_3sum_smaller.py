from bisect import bisect_left
from typing import List


class Solution:
    # TODO: two pointer approach
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                ip = bisect_left(nums, target - nums[i] - nums[j], lo=j + 1)
                ans += ip - j - 1
        return ans


s = Solution()
print(s.threeSumSmaller([-2, 0, 1, 3], target=2))
print(s.threeSumSmaller([], 0))
print(s.threeSumSmaller([0], 0))
