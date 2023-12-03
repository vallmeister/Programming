from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        ans = n + 1
        curr_sum = nums[0]
        while right < n:
            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            while right < n and curr_sum < target:
                right += 1
                if right < n:
                    curr_sum += nums[right]
        if ans > n:
            return 0
        return ans


s = Solution()
print(s.minSubArrayLen(7, nums=[2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, nums=[1, 4, 4]))
print(s.minSubArrayLen(11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
