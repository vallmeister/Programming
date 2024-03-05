from collections import defaultdict
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_length = max(length)
        ans = 0
        for i in range(n):
            if length[i] == max_length:
                ans += count[i]
        return ans


s = Solution()
print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
print(s.findNumberOfLIS([2, 2, 2, 2, 2]))
print(s.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
