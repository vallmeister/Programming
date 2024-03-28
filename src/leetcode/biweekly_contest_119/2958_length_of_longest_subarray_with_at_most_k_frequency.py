from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequencies = defaultdict(int)
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            frequencies[num] += 1
            while frequencies[num] > k:
                frequencies[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


s = Solution()
print(s.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(s.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(s.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], k=4))
