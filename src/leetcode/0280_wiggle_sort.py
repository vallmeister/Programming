class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


s = Solution()
a1 = [3, 5, 2, 1, 6, 4]
s.wiggleSort(a1)
print(a1)
a1 = [6, 6, 5, 6, 3, 8]
s.wiggleSort(a1)
print(a1)
