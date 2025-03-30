from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        m = len(pizza)
        n = len(pizza[0])
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                apples[i][j] = apples[i - 1][j] + apples[i][j - 1] - apples[i - 1][j - 1]
                if pizza[i - 1][j - 1] == 'A':
                    apples[i][j] += 1

        pass


s = Solution()
print(s.ways(pizza=["A..", "AAA", "..."], k=3))
print(s.ways(pizza=["A..", "AA.", "..."], k=3))
print(s.ways(pizza=["A..", "A..", "..."], k=1))
