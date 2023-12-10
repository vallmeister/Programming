from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            curr_streak = 1
            while num + 1 in nums:
                curr_streak += 1
                num += 1
            ans = max(ans, curr_streak)
        return ans


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
