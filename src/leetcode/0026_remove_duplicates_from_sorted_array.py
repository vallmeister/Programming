from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        i = 1
        distinct = 1
        for num in nums[1:]:
            if num != last:
                nums[i] = num
                i += 1
                last = num
                distinct += 1
        return distinct


s = Solution()
nums = [1, 1, 2]
s.removeDuplicates(nums)
print(nums)
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s.removeDuplicates(nums)
print(nums)
