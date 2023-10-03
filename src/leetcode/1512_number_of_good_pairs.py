from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for val in count.values():
            ans += val * (val - 1) // 2
        return ans


s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(s.numIdenticalPairs([1, 1, 1, 1]))
print(s.numIdenticalPairs([1, 2, 3]))
