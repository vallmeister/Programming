class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start, end = -1, -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                start = mid
                right = mid - 1
        if start == -1:
            return [start, end]
        left, right = start, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                end = mid
                left = mid + 1
        return [start, end]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))
