import bisect
import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()
        ans = []
        for spell in spells:
            target = math.ceil(success / spell)
            ip = bisect.bisect_left(potions, target)
            ans.append(m - ip)
        return ans


s = Solution()
print(s.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(s.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
