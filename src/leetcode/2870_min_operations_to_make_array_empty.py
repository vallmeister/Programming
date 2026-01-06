from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for count in counter.values():
            if count == 1:
                return -1
            ans += count // 3
            if count % 3:
                ans += 1
        return ans


s = Solution()
print(s.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(s.minOperations([2, 1, 2, 2, 3, 3]))
