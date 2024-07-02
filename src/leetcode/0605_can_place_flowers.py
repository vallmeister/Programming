from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        i = 0
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 1:
                i += 1
            elif flowerbed[i + 1] == 0:
                n -= 1
                i += 1
            i += 1
        return n <= 0
