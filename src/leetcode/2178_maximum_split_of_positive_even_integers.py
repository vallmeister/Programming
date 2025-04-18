import math
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        n = int((math.sqrt(1 + 4 * finalSum) - 1) / 2)
        ans = []
        for i in range(1, n):
            ans.append(2 * i)
            finalSum -= 2 * i
        ans.append(finalSum)
        return ans


s = Solution()
print(s.maximumEvenSplit(12))
print(s.maximumEvenSplit(7))
print(s.maximumEvenSplit(28))
