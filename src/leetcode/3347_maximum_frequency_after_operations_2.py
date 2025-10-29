import bisect
from collections import Counter
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ans = lower = 1
        upper = len(nums)
        nums.sort()
        counter = Counter(nums)
        while lower <= upper:
            mid = (upper + lower) // 2
            if self.is_possible(nums, k, numOperations, mid, counter):
                ans = mid
                lower = mid + 1
            else:
                upper = mid - 1
        return ans

    def is_possible(self, nums, k, operations, target, counter):
        for i, num in enumerate(nums):
            left = bisect.bisect_left(nums, num - k)
            right = bisect.bisect_right(nums, num + k)
            if min(right - left, operations + counter[num]) >= target:
                return True
        left = 0
        for right, num in enumerate(nums):
            while num - nums[left] > 2 * k:
                left += 1
            if min(right - left + 1, operations) >= target:
                return True
        return False


s = Solution()
print(s.maxFrequency(nums=[1, 4, 5], k=1, numOperations=2))
print(s.maxFrequency(nums=[5, 11, 20, 20], k=5, numOperations=1))
