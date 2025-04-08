from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        target = total // 2

        prev_dp = [False] * (target + 1)
        prev_dp[0] = True

        for i in reversed(range(n)):
            dp = [False] * (target + 1)
            for j in range(target + 1):
                dp[j] = prev_dp[j]
                if j >= nums[i]:
                    dp[j] |= prev_dp[j - nums[i]]
            prev_dp = dp

        return prev_dp[target]


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))
print(s.canPartition([14, 9, 8, 4, 3, 2]))
