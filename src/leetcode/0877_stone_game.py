from functools import cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @cache
        def recursive(left, right, turn):
            if right < left:
                return 0
            elif turn:
                return max(piles[left] + recursive(left + 1, right, False), piles[right],
                           recursive(left, right - 1, False))
            else:
                return min(-piles[left] + recursive(left + 1, right, True),
                           -piles[right] + recursive(left, right - 1, True))

        alice = recursive(0, n - 1, True)
        return alice > 0


s = Solution()
print(s.stoneGame([5, 3, 4, 5]))
print(s.stoneGame([3, 7, 2, 3]))
