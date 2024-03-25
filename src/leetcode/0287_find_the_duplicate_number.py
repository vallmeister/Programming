from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        cp = [0] * (n + 1)
        for i in range(n + 1):
            num = nums[i]
            cp[num] += 1
            if cp[num] > 1:
                return num
        return 0
