import math
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        fst_min = math.inf
        snd_min = math.inf
        for price in prices:
            if price < fst_min:
                fst_min, snd_min = price, fst_min
            elif price < snd_min:
                snd_min = price
        if fst_min + snd_min > money:
            return money
        else:
            return money - fst_min - snd_min


s = Solution()
print(s.buyChoco([1, 2, 2], money=3))
print(s.buyChoco([3, 2, 3], money=3))
