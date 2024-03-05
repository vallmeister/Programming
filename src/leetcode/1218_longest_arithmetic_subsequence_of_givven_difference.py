from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [1] * n
        indices = {}
        for i in range(n):
            num = arr[i]
            prev = num - difference
            if prev in indices:
                dp[i] = max(dp[i], dp[indices[prev]] + 1)
            indices[num] = i
        return max(dp)
