from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        left = 0
        right = 0
        n = len(nums)
        ans = 0
        while right < n:
            num = nums[right]
            right += 1
            window[num] += 1
            while window[num] > k:
                window[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left)
        return ans


s = Solution()
print(s.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(s.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(s.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], k=4))
