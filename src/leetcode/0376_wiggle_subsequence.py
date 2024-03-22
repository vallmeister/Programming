from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * 2 for _ in range(n)]
        lws = 0
        for i in range(n):
            num = nums[i]
            for j in range(i):
                predecessor = nums[j]
                if num > predecessor:
                    dp[i][1] = max(dp[i][1], 1 + dp[j][0])
                elif num < predecessor:
                    dp[i][0] = max(dp[i][0], 1 + dp[j][1])
            lws = max(lws, max(dp[i]))
        return lws


s = Solution()
print(s.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
print(s.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
