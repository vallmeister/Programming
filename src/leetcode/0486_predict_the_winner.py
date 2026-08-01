from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def optimal_score(i, j, is_player1):
            if i > j:
                return 0
            elif is_player1:
                return max(nums[i] + optimal_score(i + 1, j, False), nums[j] + optimal_score(i, j - 1, False))
            else:
                return min(-nums[i] + optimal_score(i + 1, j, True), -nums[j] + optimal_score(i, j - 1, True))

        return optimal_score(0, n - 1, True) >= 0


s = Solution()
print(s.predictTheWinner([1, 5, 2]))
print(s.predictTheWinner([1, 5, 233, 7]))
