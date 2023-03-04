class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray = nums[0]
        curr_subarray = nums[0]
        for num in nums[1:]:
            curr_subarray = max(num, curr_subarray + num)
            max_subarray = max(max_subarray, curr_subarray)
        return max_subarray


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
