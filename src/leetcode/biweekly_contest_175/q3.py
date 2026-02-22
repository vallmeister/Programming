import bisect
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            mask = 1 << i
            sequence = list(filter(lambda num: num & mask, nums))
            ans = max(ans, self.get_lis(sequence))
        return ans

    def get_lis(self, nums):
        lis = []
        for num in nums:
            i = bisect.bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num
        return len(lis)


s = Solution()
print(s.longestSubsequence(nums=[5, 4, 7]))
print(s.longestSubsequence(nums=[2, 3, 6]))
print(s.longestSubsequence(nums=[0, 1]))
print(s.longestSubsequence(nums=[12, 4, 7]))
