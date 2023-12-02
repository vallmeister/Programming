from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix = [0] * n
        prefix[1] = nums[0]
        suffix = [0] * n
        for i in range(2, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix[-2] = nums[-1]
        for i in range(n - 3, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        ans[0] = suffix[0]
        ans[-1] = prefix[-1]
        for i in range(1, n - 1):
            ans[i] = prefix[i] * suffix[i]
        return ans

    def product_except_self_optimized(self, nums):
        n = len(nums)
        ans = [0] * n
        ans[1] = nums[0]
        for i in range(2, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        suffix = nums[-1]
        for i in range(n - 2, 0, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        ans[0] = suffix
        return ans


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
print(s.product_except_self_optimized([1, 2, 3, 4]))
print(s.product_except_self_optimized([-1, 1, 0, -3, 3]))
