from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        while True:
            operation_performed = False
            for i in range(n - 1):
                if nums[i] > nums[i + 1] and nums[i].bit_count() == nums[i + 1].bit_count():
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    operation_performed = True
                    break
            if not operation_performed:
                break
        return all(nums[i] <= nums[i + 1] for i in range(n - 1))


s = Solution()
print(s.canSortArray([8, 4, 2, 30, 15]))
print(s.canSortArray([1, 2, 3, 4, 5]))
print(s.canSortArray([3, 16, 8, 4, 2]))
