from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[j] > nums[i] and nums[i].bit_count() != nums[j].bit_count():
                    return False
        return True

    def can_sort_array_segment(self, nums):
        curr_bits = nums[0].bit_count()
        curr_min = curr_max = nums[0]
        prev_max = 0
        for num in nums[1:]:
            if num.bit_count() == curr_bits:
                curr_min = min(curr_min, num)
                curr_max = max(curr_max, num)
            else:
                curr_bits = num.bit_count()
                prev_max = curr_max
                curr_max = curr_min = num
            if curr_min < prev_max:
                return False
        return True


s = Solution()
print(s.canSortArray([8, 4, 2, 30, 15]))
print(s.canSortArray([1, 2, 3, 4, 5]))
print(s.canSortArray([3, 16, 8, 4, 2]))

print(s.can_sort_array_segment([8, 4, 2, 30, 15]))
