from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ms = []
        for j in range(len(prices)):
            while ms and prices[ms[-1]] >= prices[j]:
                prices[ms.pop()] -= prices[j]
            ms.append(j)
        return prices


s = Solution()
print(s.finalPrices([8, 4, 6, 2, 3]))
print(s.finalPrices([1, 2, 3, 4, 5]))
print(s.finalPrices([10, 1, 1, 6]))
