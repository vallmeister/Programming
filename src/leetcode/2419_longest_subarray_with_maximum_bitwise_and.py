from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] == mx:
                curr += 1
            else:
                curr = 1
            ans = max(ans, curr)
        return ans


s = Solution()
print(s.longestSubarray([1, 2, 3, 3, 2, 2]))
