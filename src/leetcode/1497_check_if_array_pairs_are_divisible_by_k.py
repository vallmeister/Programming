from collections import defaultdict
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pair_freq = defaultdict(int)
        for num in arr:
            r = ((num % k) + k) % k
            pair_freq[r] += 1
        for i in range(k):
            if (i == 0 or i == k - i) and pair_freq[i] % 2:
                return False
            elif i > 0 and pair_freq[i] != pair_freq[k - i]:
                return False
        return True


s = Solution()
print(s.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
