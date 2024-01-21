from typing import List


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        nums.sort()
        while nums[0] < nums[-1]:
            nums.pop()
        print(nums)
        return (len(nums) + 1) // 2


s = Solution()
print(s.minimumArrayLength([1, 4, 3, 1]))
print(s.minimumArrayLength([5, 5, 5, 10, 5]))
print(s.minimumArrayLength([2, 3, 4]))
print(s.minimumArrayLength([5, 2, 2, 2, 9, 10]))
