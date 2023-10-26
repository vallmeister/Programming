from collections import defaultdict
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        unique_numbers = set(arr)
        dp = {num: 1 for num in arr}
        for i in arr:
            for j in arr:
                if i % j == 0 and i // j in unique_numbers:
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[i // j]
        return sum(dp.values()) % (10 ** 9 + 7)


s = Solution()
print(s.numFactoredBinaryTrees([2, 4]))
print(s.numFactoredBinaryTrees([2, 4, 5, 10]))
print(s.numFactoredBinaryTrees([18, 3, 6, 2]))
