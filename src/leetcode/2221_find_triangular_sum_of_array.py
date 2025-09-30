from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            tmp = []
            n = len(nums)
            for i in range(1, n):
                tmp.append((nums[i] + nums[i - 1]) % 10)
            nums = tmp
        return nums[0]


s = Solution()
print(s.triangularSum([1, 2, 3, 4, 5]))
print(s.triangularSum([5]))
