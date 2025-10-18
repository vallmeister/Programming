from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = lower = 1
        upper = n // 2
        while lower <= upper:
            mid = (upper + lower) // 2
            if self.bin_search(nums, mid):
                ans = mid
                lower = mid + 1
            else:
                upper = mid - 1
        return ans

    def get_prefix_sum(self, nums):
        n = len(nums)
        ps = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                ps[i] = 1
        return ps

    def bin_search(self, nums, target):
        n = len(nums)
        ps = self.get_prefix_sum(nums)
        left = 0
        t1 = t2 = 0
        for right in range(target - 1):
            t1 += ps[right]
            t2 += ps[right + target]
        for right in range(target - 1, n - target):
            t1 += ps[right]
            t2 += ps[right + target]
            t1 -= ps[left]
            t2 -= ps[left + target]
            left += 1
            if t1 >= target - 1 and t2 >= target - 1:
                return True
        return False


s = Solution()
print(s.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(s.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
