class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return i


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
