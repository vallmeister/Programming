from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lower = 1
        upper = ans = max(quantities)
        while lower <= upper:
            mid = (upper + lower) // 2
            stores = 0
            for q in quantities:
                stores += ceil(q / mid)
            if stores > n:
                lower = mid + 1
            else:
                ans = min(ans, mid)
                upper = mid - 1
        return ans
