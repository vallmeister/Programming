from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        prev = nums[0]
        for num in nums[1:]:
            if prev == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                prev = num
                count = 1
        return prev


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
