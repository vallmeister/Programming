from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pairs = 0
        count = defaultdict(int)
        for i, num in enumerate(nums):
            good_pairs += count[num - i]
            count[num - i] += 1
        return n * (n - 1) // 2 - good_pairs


s = Solution()
print(s.countBadPairs([4, 1, 3, 3]))
print(s.countBadPairs([1, 2, 3, 4, 5]))
