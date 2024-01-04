from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if 1 in counter.values():
            return -1
        ans = 0
        for count in counter.values():
            if count == 2:
                ans += 1
            elif count % 3 == 0:
                ans += count // 3
            elif count % 3 == 1:
                ans += 2
                count -= 2 * 2
                ans += count // 3
            elif count % 3 == 2:
                ans += 1
                ans += count // 3
        return ans


s = Solution()
print(s.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(s.minOperations([2, 1, 2, 2, 3, 3]))
