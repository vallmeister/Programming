from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        ans[0] = prefix[-1] - prefix[0] - (n - 1) * nums[0]
        for i in range(1, n):
            ans[i] = i * nums[i] - prefix[i - 1] + prefix[-1] - prefix[i] - (n - i - 1) * nums[i]
        return ans


s = Solution()
print(s.getSumAbsoluteDifferences([2, 3, 5]))
print(s.getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
