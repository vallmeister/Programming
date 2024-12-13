from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        lower = 1
        upper = max(ribbons)
        ans = 0
        while lower <= upper:
            mid = (lower + upper) // 2
            if self.is_valid(ribbons, mid) >= k:
                ans = max(ans, mid)
                lower = mid + 1
            else:
                upper = mid - 1
        return ans

    def is_valid(self, ribbons, length):
        count = 0
        for r in ribbons:
            count += r // length
        return count
