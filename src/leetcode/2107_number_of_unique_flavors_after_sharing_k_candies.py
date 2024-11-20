from collections import Counter
from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counter = Counter(candies)
        if k == 0:
            return len(counter.keys())
        ans = 0
        for candy in candies[:k - 1]:
            counter[candy] -= 1
            if counter[candy] == 0:
                del counter[candy]
        left = 0
        for candy in candies[k - 1:]:
            counter[candy] -= 1
            if counter[candy] == 0:
                del counter[candy]
            ans = max(ans, len(counter.keys()))
            counter[candies[left]] += 1
            left += 1
        return ans


s = Solution()
print(s.shareCandies([2, 2, 2, 2, 3, 3], 2))
print(s.shareCandies([1, 1, 2, 1], 2))
