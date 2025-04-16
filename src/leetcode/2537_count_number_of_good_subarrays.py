from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        window = 0
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            window += freq[num]
            freq[num] += 1
            while window >= k:
                ans += n - right
                freq[nums[left]] -= 1
                window -= freq[nums[left]]
                left += 1
        return ans
