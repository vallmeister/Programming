from collections import Counter
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        major_count = max(counter.values())
        lower = n % 2
        return max(lower, major_count - (n - major_count))


s = Solution()
print(s.minLengthAfterRemovals(nums=[1, 2, 3, 4]))
print(s.minLengthAfterRemovals(nums=[1, 1, 2, 2, 3, 3]))
print(s.minLengthAfterRemovals(nums=[1000000000, 1000000000]))
print(s.minLengthAfterRemovals(nums=[1, 2, 3, 4, 5]))
print(s.minLengthAfterRemovals(nums=[2, 3, 4, 4, 4]))
