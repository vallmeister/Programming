import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = 0
        closest_diff = math.inf
        for j in range(n-1, -1, -1):
            for i in range(0, j):
                left = i + 1
                right = j - 1
                while left <= right:
                    mid = (left + right) // 2
                    three_sum = nums[i] + nums[j] + nums[mid]
                    diff = abs(target - three_sum)
                    if diff < closest_diff:
                        closest_diff = diff
                        closest_sum = three_sum
                    if three_sum < target:
                        left = mid + 1
                    elif three_sum == target:
                        return three_sum
                    elif three_sum > target:
                        right = mid - 1
        return closest_sum


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], target=1))
print(s.threeSumClosest([0, 0, 0], target=1))
