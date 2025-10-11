import bisect
from collections import Counter
from functools import cache
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        power = sorted(freq.keys())
        n = len(power)

        @cache
        def memo(i):
            if i >= n:
                return 0
            no_take = memo(i + 1)
            p = power[i]
            j = bisect.bisect_left(power, p + 3)
            take = p * freq[p] + memo(j)
            return max(take, no_take)

        return memo(0)


s = Solution()
print(s.maximumTotalDamage(power=[1, 1, 3, 4]))
print(s.maximumTotalDamage(power=[7, 1, 6, 6]))
