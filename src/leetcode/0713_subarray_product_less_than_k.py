from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        product = 1
        left = 0
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


s = Solution()
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
