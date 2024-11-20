from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        count = 0
        for i in range(1, k - 1):
            if nums[i] - nums[i - 1] == 1:
                count += 1
        for right in range(k - 1, n):
            if right > 0 and nums[right] - nums[right - 1] == 1:
                count += 1
            if right - k + 1 > 0 and nums[right - k + 1] - nums[right - k] == 1:
                count -= 1
            if count == k - 1:
                ans.append(nums[right])
            else:
                ans.append(-1)
        return ans


s = Solution()
print(s.resultsArray([3, 2, 3, 2, 3, 2], 2))
