import math


class Solution:
    def countElements(self, nums: list[int]) -> int:
        max_so_far = -math.inf
        min_so_far = math.inf
        max_count = 0
        min_count = 0
        for num in nums:
            if num > max_so_far:
                max_so_far = num
                max_count = 1
            elif num == max_so_far:
                max_count += 1
            if num < min_so_far:
                min_so_far = num
                min_count = 1
            elif num == min_so_far:
                min_count += 1
        return max(len(nums) - max_count - min_count, 0)


s = Solution()
print(s.countElements([11, 7, 2, 15]))
print(s.countElements([-3, 3, 3, 90]))
