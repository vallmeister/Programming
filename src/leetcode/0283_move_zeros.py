class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        while i < n and j < n:
            if i >= j:
                j += 1
            elif nums[j] == 0:
                j += 1
            elif nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                i += 1

    def move_zeros(self, nums):
        last_non_zero_found_at = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[last_non_zero_found_at], nums[curr] = nums[curr], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1


s = Solution()
l1 = [0, 1, 0, 3, 12]
s.moveZeroes(l1)
print(l1)
l2 = [0]
s.moveZeroes(l2)
print(l2)
l1 = [0, 1, 0, 3, 12]
s.move_zeros(l1)
print(l1)
