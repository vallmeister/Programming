class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums

    def sorted_quares_two_pointers(self, nums):
        left = 0
        right = len(nums) - 1
        ans = []
        for _ in range(len(nums)):
            if abs(nums[left]) > abs(nums[right]):
                ans.append(nums[left] ** 2)
                left += 1
            else:
                ans.append(nums[right] ** 2)
                right -= 1
        return ans[::-1]


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
print(s.sortedSquares([-7, -3, 2, 3, 11]))
print(s.sorted_quares_two_pointers([-4, -1, 0, 3, 10]))
print(s.sorted_quares_two_pointers([-7, -3, 2, 3, 11]))
