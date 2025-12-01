from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = n - 1
            for j in range(i + 1, n):
                while k >= 0 and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                ans += max(0, k - j)
        return ans


s = Solution()
print(s.threeSumSmaller([-2, 0, 1, 3], target=2))
print(s.threeSumSmaller([], 0))
print(s.threeSumSmaller([0], 0))
print(s.threeSumSmaller([1, -1, 2, 0, 3, -2], 2))
