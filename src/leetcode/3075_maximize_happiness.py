from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += max(0, happiness[i] - i)
        return ans


s = Solution()
print(s.maximumHappinessSum(happiness=[1, 2, 3], k=2))
print(s.maximumHappinessSum(happiness=[1, 1, 1, 1], k=2))
print(s.maximumHappinessSum(happiness=[2, 3, 4, 5], k=1))
