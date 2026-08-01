class Solution:
    def findMin(self, nums: list[int]) -> int:
        return self.divide_and_conquer(nums, 0, len(nums) - 1)

    def divide_and_conquer(self, nums, left, right):
        n = right - left + 1
        if n == 1 or nums[left] < nums[right]:
            return nums[left]
        mid = left + (right - left) // 2
        return min(self.divide_and_conquer(nums, left, mid), self.divide_and_conquer(nums, mid + 1, right))


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
