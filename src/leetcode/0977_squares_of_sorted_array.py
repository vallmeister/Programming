class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        for i in reversed(range(n)):
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left] ** 2
                left += 1
            else:
                ans[i] = nums[right] ** 2
                right -= 1
        return ans


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
print(s.sortedSquares([-7, -3, 2, 3, 11]))
print(s.sortedSquares([-5, -3, -2, -1]))
