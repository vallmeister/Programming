class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        result = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for curr in nums[1:]:
            tmp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, min_so_far * curr, max_so_far * curr)

            max_so_far = tmp_max
            result = max(max_so_far, result)
        return result


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([5, -3, 5]))
print(s.maxProduct([5, -3, 5, 0, -3, -2, 5]))
print(s.maxProduct([5, -3, -4, 0, 5]))
print(s.maxProduct([2, -5, -2, -4, 3]))
