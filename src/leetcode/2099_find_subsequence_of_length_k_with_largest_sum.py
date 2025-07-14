from collections import Counter
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        count = Counter(list(sorted(nums, reverse=True))[:k])
        ans = []
        for num in nums:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1
        return ans


s = Solution()
print(s.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(s.maxSubsequence(nums=[-1, -2, 3, 4], k=3))
print(s.maxSubsequence(nums=[3, 4, 3, 3], k=2))
