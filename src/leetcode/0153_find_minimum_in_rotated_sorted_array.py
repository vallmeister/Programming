import math


class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_so_far = math.inf

        def binary_search(start, end):
            nonlocal min_so_far
            mid = (start + end) // 2
            if start > end:
                return
            elif nums[start] <= nums[mid]:
                min_so_far = min(min_so_far, nums[start])
                binary_search(mid + 1, end)
            else:
                min_so_far = min(min_so_far, nums[mid])
                binary_search(start, mid - 1)

        binary_search(0, len(nums) - 1)
        return min_so_far


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
