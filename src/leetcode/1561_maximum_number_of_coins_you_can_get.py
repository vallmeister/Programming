from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        n = len(piles)
        piles.sort(reverse=True)
        for i in range(1, 2 * n // 3, 2):
            ans += piles[i]
        return ans


s = Solution()
print(s.maxCoins([2, 4, 1, 2, 7, 8]))
print(s.maxCoins([2, 4, 5]))
print(s.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
