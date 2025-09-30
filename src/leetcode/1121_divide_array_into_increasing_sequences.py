from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        prev = nums[0]
        occ = 1
        max_occ = len(nums) // k
        for num in nums[1:]:
            if num == prev:
                occ += 1
            else:
                occ = 1
                prev = num
            if max_occ < occ:
                return False
        return True


s = Solution()
print(s.canDivideIntoSubsequences(nums=[1, 2, 2, 3, 3, 4, 4], k=3))
print(s.canDivideIntoSubsequences(nums=[5, 6, 6, 7, 8], k=3))
