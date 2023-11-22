from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dfs(i, j, player_one):
            if i > j:
                return 0
            elif player_one:
                return max(nums[i] + dfs(i + 1, j, False), nums[j] + dfs(i, j - 1, False))
            else:
                return min(-nums[i] + dfs(i + 1, j, True), -nums[j] + dfs(i, j - 1, True))

        return dfs(0, n - 1, True) >= 0

    def predict_winner_dp(self, nums):
        n = len(nums)
        player_one = [[0] * (n + 1) for _ in range(n + 1)]
        player_two = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            player_one[i][i] = nums[i]
            player_two[i][i] = -nums[i]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                player_one[i][j] = max(nums[i] + player_two[i + 1][j], nums[j] + player_two[i][j - 1])
                player_two[i][j] = min(-nums[i] + player_one[i + 1][j], -nums[j] + player_one[i][j - 1])
        return player_one[0][n - 1] >= player_two[0][n - 1]


s = Solution()
print(s.predictTheWinner([1, 5, 2]))
print(s.predictTheWinner([1, 5, 233, 7]))
print(s.predict_winner_dp([1, 5, 2]))
print(s.predictTheWinner([1, 5, 233, 7]))
