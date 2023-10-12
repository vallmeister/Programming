# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # 1. Find peak element
        left = 1
        right = n - 2
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak_index = left
        # 2. Search in the left part, which is strictly increasing, for target
        left = 0
        right = peak_index
        while left <= right:
            mid = (left + right) // 2
            element = mountain_arr.get(mid)
            if element == target:
                return mid
            elif element < target:
                left = mid + 1
            elif target < element:
                right = mid - 1
        # 3. Search in the right part, which is strictly decreasing, for target
        left = peak_index + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            element = mountain_arr.get(mid)
            if target == element:
                return mid
            elif element > target:
                left = mid + 1
            elif target > element:
                right = mid - 1
        return -1
