from typing import List


class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(express)
        ans = []
        dp = [0, expressCost]
        for i in range(n):
            dp = [min(dp) + regular[i], min(dp[1], dp[0] + expressCost) + express[i]]
            ans.append(min(dp))
        return ans


s = Solution()
print(s.minimumCosts(regular=[1, 6, 9, 5], express=[5, 2, 3, 10], expressCost=8))
