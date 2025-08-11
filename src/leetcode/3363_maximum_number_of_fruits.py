import math
from functools import cache
from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        @cache
        def memo_player2(i, j):
            if i == j == n - 1:
                return 0
            elif j >= n or j <= i:
                return -math.inf
            return fruits[i][j] + max(memo_player2(i + 1, j - 1), memo_player2(i + 1, j), memo_player2(i + 1, j + 1))

        @cache
        def memo_player3(i, j):
            if i == j == n - 1:
                return 0
            elif i >= n or i <= j:
                return -math.inf
            return fruits[i][j] + max(memo_player3(i - 1, j + 1), memo_player3(i, j + 1), memo_player3(i + 1, j + 1))

        # memo = {}
        #
        # def memo_general(i, j, comparison, transition):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     elif i == j == n - 1:
        #         return 0
        #     elif i >= n or j >= n or comparison(i, j):
        #         return -math.inf
        #     memo[(i, j)] = fruits[i][j] + max(
        #         memo_general(ii, jj, comparison, transition) for ii, jj in transition(i, j))
        #     return memo[(i, j)]

        return sum(fruits[i][i] for i in range(n)) + memo_player2(0, n - 1) + memo_player3(n - 1, 0)
        # return (sum(fruits[i][i] for i in range(n))
        #         + memo_general(0, n - 1, lambda x, y: y <= x,
        #                        lambda x, y: [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)])
        #         + memo_general(n - 1, 0, lambda x, y: x <= y,
        #                        lambda x, y: [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]))


s = Solution()
print(s.maxCollectedFruits(fruits=[[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(s.maxCollectedFruits([[1, 1], [1, 1]]))
