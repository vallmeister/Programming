from collections import Counter
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_frequency = 0
        left = 0
        n = len(nums)
        curr = 0

        for right in range(n):
            target = nums[right]
            curr += target

            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            max_frequency = max(max_frequency, right - left + 1)

        return max_frequency


s = Solution()
print(s.maxFrequency([1, 2, 4], k=5))
print(s.maxFrequency([1, 4, 8, 13], k=5))
print(s.maxFrequency([3, 9, 6], k=2))
