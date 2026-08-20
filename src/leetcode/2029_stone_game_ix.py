from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt_0 = cnt_1 = cnt_2 = 0
        for stone in stones:
            if stone % 3 == 0:
                cnt_0 += 1
            elif stone % 3 == 1:
                cnt_1 += 1
            elif stone % 3 == 2:
                cnt_2 += 1
        pass
