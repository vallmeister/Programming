from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                ans.append(abs(nums[i]))
            nums[j] = -nums[j]
        return ans
