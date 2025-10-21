from typing import List
from collections import Counter
import bisect


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        counter = Counter(nums)
        nums.sort()
        n = len(nums)
        ans = 1
        for i in range(nums[0], nums[-1] + 1):
            left = bisect.bisect_left(nums, i - k)
            right = bisect.bisect_right(nums, i + k)
            ans = max(ans, min(counter[i] + numOperations, right - left))
        return ans


s = Solution()
print(s.maxFrequency(nums = [1,4,5], k = 1, numOperations = 2))
print(s.maxFrequency(nums = [5,11,20,20], k = 5, numOperations = 1))
print(s.maxFrequency([23, 54], 77, 1))
