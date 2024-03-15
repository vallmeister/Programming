from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pp = [1] * n
        sp = [1] * n
        for i in range(1, n):
            pp[i] = pp[i - 1] * nums[i - 1]
        for i in reversed(range(n - 1)):
            sp[i] = sp[i + 1] * nums[i + 1]
        ans = [0] * n
        for i in range(n):
            ans[i] = pp[i] * sp[i]
        return ans


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
