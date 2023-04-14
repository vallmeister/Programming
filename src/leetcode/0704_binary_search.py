class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lower = 0
        upper = len(nums)
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = max(mid, lower + 1)
            elif nums[mid] > target:
                upper = min(mid, upper - 1)
        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
print(s.search([5], 5))
