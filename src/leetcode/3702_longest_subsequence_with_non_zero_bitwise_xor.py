from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        zeroes = 0
        for num in nums:
            xor ^= num
            if num == 0:
                zeroes += 1
        if zeroes == n:
            return 0
        elif xor == 0:
            return n - 1
        else:
            return n


s = Solution()
print(s.longestSubsequence([1, 2, 3]))
print(s.longestSubsequence([2, 3, 4]))
print(s.longestSubsequence([0, 0, 7, 0, 0, 0, 7, 0, 0]))
