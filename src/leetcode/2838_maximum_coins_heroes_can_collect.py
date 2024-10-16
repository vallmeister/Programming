from typing import List


class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        monsters = list(sorted(zip(monsters, coins)))
        heroes = list(sorted(enumerate(heroes), key=lambda x: x[1]))
        m = len(monsters)
        n = len(heroes)
        j = 0
        ans = [0] * n
        prev_index = -1
        for idx, hero in heroes:
            ans[idx] += ans[prev_index]
            while j < m and monsters[j][0] <= hero:
                ans[idx] += monsters[j][1]
                j += 1
            prev_index = idx
        return ans


s = Solution()
print(s.maximumCoins(heroes=[1, 4, 2], monsters=[1, 1, 5, 2, 3], coins=[2, 3, 4, 5, 6]))
