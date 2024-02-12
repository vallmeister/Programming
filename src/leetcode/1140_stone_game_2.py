from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        total = sum(piles)

        @cache
        def recursive(idx, m, turn):
            if idx >= n:
                return 0
            if turn:
                result = 0
                for x in range(1, min(n - idx, 2 * m) + 1):
                    result = max(sum(piles[idx:idx + x]) + recursive(idx + x, max(x, m), not turn), result)
                return result
            else:
                result = total
                for x in range(1, min(n - idx, 2 * m) + 1):
                    result = min(recursive(idx + x, max(x, m), not turn), result)
                return result

        return recursive(0, 1, True)


s = Solution()
print(s.stoneGameII([2, 7, 9, 4, 4]))
