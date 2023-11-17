from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_so_far = 0
        nums.sort()
        n = len(nums)
        j = n - 1
        for i in range(n // 2):
            max_so_far = max(max_so_far, nums[i] + nums[j])
            j -= 1
        return max_so_far


s = Solution()
print(s.minPairSum([3, 5, 2, 3]))
print(s.minPairSum([3, 5, 4, 2, 4, 6]))
