from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        left = 0
        subarray_sum = 0
        for right in range(n):
            subarray_sum += nums[right]
            while subarray_sum >= target:
                if not ans or ans > right - left + 1:
                    ans = right - left + 1
                subarray_sum -= nums[left]
                left += 1
        return ans


s = Solution()
print(s.minSubArrayLen(7, nums=[2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, nums=[1, 4, 4]))
print(s.minSubArrayLen(11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
