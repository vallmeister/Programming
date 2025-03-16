from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        ans = n + 1
        seen = {}
        for i, card in enumerate(cards):
            if card in seen:
                ans = min(ans, i - seen[card] + 1)
            seen[card] = i

        return -1 if ans == n + 1 else ans
