from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        ps = 0
        prev = {0: -1}
        for i, num in enumerate(nums):
            ps += num
            if ps - k in prev:
                ans = max(ans, i - prev[ps - k])
            if ps not in prev:
                prev[ps] = i
        return ans


s = Solution()
print(s.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
print(s.maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))
