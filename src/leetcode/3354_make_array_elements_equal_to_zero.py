from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
        right = [0] * n
        for i in reversed(range(n - 1)):
            right[i] = right[i + 1] + nums[i + 1]
        ans = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            elif right[i] == left[i]:
                ans += 2
            elif abs(right[i] - left[i]) == 1:
                ans += 1
        return ans


s = Solution()
print(s.countValidSelections(nums=[1, 0, 2, 0, 3]))
print(s.countValidSelections(nums=[2, 3, 4, 0, 4, 1, 0]))
