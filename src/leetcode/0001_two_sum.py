from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {num: idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            if target - num in dictionary:
                if idx != dictionary[target - num]:
                    return [idx, dictionary[target - num]]
        return [-1, -1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
