from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ordering = [0] * n
        skip = False
        index_in_deck = 0
        index_in_ordering = 0
        while index_in_deck < n:
            if ordering[index_in_ordering] == 0:
                if not skip:
                    ordering[index_in_ordering] = deck[index_in_deck]
                    index_in_deck += 1
                skip = not skip
            index_in_ordering += 1
            index_in_ordering %= n
        return ordering


s = Solution()
print(s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
