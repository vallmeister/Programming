from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n - 1
        first, last = -1, -2

        # find left-most index of target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                first = mid
                right = mid - 1

        # find right-most index of target
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                last = mid
                left = mid + 1

        return last - first + 1 > n // 2
