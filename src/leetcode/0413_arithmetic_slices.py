class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            diff = nums[j] - nums[i]
            j += 1
            while j < n and nums[j] - nums[j - 1] == diff:
                result += 1
                j += 1
        return result


s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
print(s.numberOfArithmeticSlices([1]))
