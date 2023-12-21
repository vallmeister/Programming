class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = nums[0]
        ans = curr_sum
        for num in nums[1:]:
            curr_sum = max(curr_sum + num, num)
            ans = max(ans, curr_sum)
        return ans


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
