from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        items = list(zip(ages, scores))
        items.sort()
        dp = [0] * n
        for i in range(n):
            age, score = items[i]
            for j in range(i):
                _, prev_score = items[j]
                if prev_score <= score:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += score

        return max(dp)


s = Solution()
print(s.bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]))
print(s.bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]))
print(s.bestTeamScore(scores=[1, 2, 3, 5], ages=[8, 9, 10, 1]))
print(s.bestTeamScore([9, 2, 8, 8, 2], [4, 1, 3, 3, 5]))
