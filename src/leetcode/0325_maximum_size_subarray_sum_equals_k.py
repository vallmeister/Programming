from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        ps = [0] * (n + 1)
        ps[0] = nums[0]
        for i in range(n):
            ps[i] = ps[i - 1] + nums[i]
        h = {}
        for right in range(n):
            if ps[right] == k:
                ans = max(ans, right + 1)
            elif ps[right] - k in h:
                left = h[ps[right] - k]
                ans = max(ans, right - left)
            if ps[right] not in h:
                h[ps[right]] = right
        return ans
