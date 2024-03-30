from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def sliding_window_with_at_most_k_elements(k1):
            left = 0
            ans = 0
            window = {}
            for right, num in enumerate(nums):
                if num not in window:
                    window[num] = 0
                window[num] += 1
                while len(window.keys()) > k1:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                    left += 1
                ans += right - left + 1
            return ans

        return sliding_window_with_at_most_k_elements(k) - sliding_window_with_at_most_k_elements(k - 1)


s = Solution()
print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], k=2))
print(s.subarraysWithKDistinct([1, 2, 1, 3, 4], k=3))
print(s.subarraysWithKDistinct([2, 1, 2, 1, 1], 3))
print(s.subarraysWithKDistinct([2, 2, 1, 2, 2, 2, 1, 1], 2))
