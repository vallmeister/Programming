from functools import cache
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def recursive(i, curr_height, curr_width):
            if i == n:
                return curr_height
            thickness, height = books[i]
            if curr_width + thickness > shelfWidth:
                return curr_height + recursive(i + 1, height, thickness)
            else:
                return min(curr_height + recursive(i + 1, height, thickness),
                           recursive(i + 1, max(height, curr_height), curr_width + thickness))

        return recursive(0, 0, 0)
