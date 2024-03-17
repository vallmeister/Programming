import math
from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        a = len(strs)

        @cache
        def memo(i, ms, ns):
            if ms < 0 or ns < 0:
                return -math.inf
            elif i >= a:
                return 0
            return max(1 + memo(i + 1, ms - strs[i].count('0'), ns - strs[i].count('1')), memo(i + 1, ms, ns))

        return memo(0, m, n)


s = Solution()
print(s.findMaxForm(["10", "0001", "111001", "1", "0"], m=5, n=3))
print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 50, 50))
