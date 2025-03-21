from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1
        left = 0
        window = [0] * 32
        for right, num in enumerate(nums):
            self.add_bits(window, num, 1)
            while any(bit > 1 for bit in window):
                self.add_bits(window, nums[left], -1)
                left += 1
            ans = max(ans, right - left + 1)

        return ans

    def add_bits(self, window, num, sign):
        for i in range(32):
            mask = 1 << i
            if mask & num:
                window[i] += 1 * sign


s = Solution()
print(s.longestNiceSubarray([1, 3, 8, 48, 10]))
print(s.longestNiceSubarray([3, 1, 5, 11, 13]))
