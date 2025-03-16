from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = ans = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.check_capability(nums, k, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def check_capability(self, nums, k, capability):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[n - 1] = 1 if nums[n - 1] <= capability else 0
        for i in reversed(range(n - 1)):
            if nums[i] <= capability:
                dp[i] = max(dp[i + 1], 1 + dp[i + 2])
            else:
                dp[i] = dp[i + 1]
        return dp[0] >= k


s = Solution()
print(s.minCapability(nums=[2, 3, 5, 9], k=2))
print(s.minCapability(nums=[2, 7, 9, 3, 1], k=2))
