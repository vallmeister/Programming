from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        nums2 = nums * 2
        is_sorted = False
        for i in range(n):
            for j in range(i + 1, i + n):
                if nums2[j - 1] > nums2[j]:
                    break
            else:
                is_sorted = True
        if not is_sorted:
            return -1
        return (n - nums.index(min(nums))) % n


s = Solution()
print(s.minimumRightShifts(nums=[3, 4, 5, 1, 2]))
print(s.minimumRightShifts(nums=[1, 3, 5]))
print(s.minimumRightShifts(nums=[2, 1, 4]))
