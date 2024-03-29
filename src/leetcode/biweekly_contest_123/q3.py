import math
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -math.inf
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + nums[i - 1]
        last = {}
        for end, num in enumerate(nums):
            curr_array = -math.inf
            if num + k in last:
                start = last[num + k]
                curr_array = ps[end + 1] - ps[start]
            if num - k in last:
                start = last[num - k]
                curr_array = max(curr_array, ps[end + 1] - ps[start])
            ans = max(ans, curr_array)

            if num not in last or num in last and ps[end] - ps[last[num]] <= 0:
                last[num] = end

        return ans if ans > -math.inf else 0


s = Solution()
print(s.maximumSubarraySum([1, 2, 3, 4, 5, 6], k=1))
print(s.maximumSubarraySum([-1, 3, 2, 4, 5], k=3))
print(s.maximumSubarraySum([-1, -2, -3, -4], k=2))
print(s.maximumSubarraySum(
    [-10, 4, 6, 6, -7, 0, -10, -5, 10, 10, -1, -7, 4, -9, 1, -4, 3, -5, 1, 8, -5, 8, 7, 10, 5, 0, -5, -10, -3, -2, 5,
     -10, 8, 9, -3, -6, -1, 9, 4, 4, -8, -5, 3, 3, 2, -10, 2, 5, 1, -7, -2, -8, 7, -7, -9, -1, 1, -7, -6, 7, 7, 2, -1,
     4, -7, -8, -2, -5, 6, -6, -7, 9, -6, -1, -5, -9, 3, 9, 1, -5, -8, -8, -10, 10, -5, 8, -8, 1, 10, -5, 10, 1, -5, 0,
     -7, -7, -5, -10, 3, 3, 1, 9, -5, 0, 6, -5, -9, 7, 0, -2, 5, 2, -8, 0, 2, 10, 9, 8, 9, 10, -8, 5, -7, 6, 9, 4, -10,
     -10, 3, -4, -7, 2, 0, 8, 8, -3, -10, -1, 4, -6, -10, -7, -4, -9, -10, 4, 7, -1, 10, -2, 2, -6, -7, 4, -7, -2, -7,
     -5, -9, 5, -3, -7, 8, -1, -3, 9, 3, -2, -3, 10, 0, 7, -5, 10, 2, -6, -4, 7, 8, -7, 4, -3, 2, -3, 5, 1, 5, 10, -2,
     -2, -2, -6, -8, -1, 8, -7, 5, 10, 7, -8, 0, 7, -5, 3, 10, 3, 0, -1, 5, -4, -1, 0, -8, -8, 8, 6, 4, 9, -7, 5, 10,
     -1, -7, 10, -5, -10, 10, 7, 6, -5, -1, -9, -4, -5, -9, 3, -10, 3, 9, 2, 0, -5, 10, 8, 8, 6, -2, -6, 2, -4, -8, -3,
     6, -4, 3, 9, -4, -5, -9, -1, -9, -7, -7, 5, 2, -6, -8, -4, 5, -5, 2, 1, -6, -10, -1, -8, 7, 1, 0, -2, -6, -9, 0,
     -8, -1, -5, -3, 2, -4, 7, -10, -6, -7, -8, 2, 1, -4, -3, -7, -5, -10, -4, -7, -2, -9, -1, -1, -1, -4, -6, -5, -5,
     8, 9, -2, 5, -9, -9, -6, -7, 10, -9, -10, -10, -7, -7, -9, -8, 4, 10, -6, -10, 3, 0, -5, -9, -4, -4, 1, 0, -9, 7,
     9, -7, -5, 2, 7, 6, 3, -6, 4, -5, -2, -10, 8, -7, -5, -8, 10, 0, -9, 5, 1, -4, -4, -6, 5, 10, 9, 8, -3, 8, -2, -2,
     5, 10, -2, 3, 3, -9, 5, 3, -8, 8, 0, 7, 3, -4, -1, 10, -6, -1, -8, 1, 6, -7, 8, -9, 7, -10, -6, -10, -1, 8, 1, 10,
     9, -7, -2, 6, -1, 2, 10, -10, -3, -6, 4, 2, -1, 1, -10, 5, 1, -4, 1, 5, 3, 6, 2, 10, -8, 10, -2, -8, 1, -5, -5, 1,
     6, 2, -10, -2, -7, -9, 0, -6, -7, 1, 8, -1, -10, 9, -10, 9, -2, 10, 2, 8, -8, 8, 10, 0, 2, -9, 1, 5, 8, -7, 1, 5,
     -9, -1, 3, -4, 4, -4, -10, 1, -5, -8, 9, 5, 7, -4, -10, -3, 10, -9, -1, 6, 7, -9, -10, 5, -1, -6, 7, 4, 4, 2, -9,
     8, -5, 10, 5, -1, -7, 3, 6, 8, 8, 4, -10, 1, -10, -2, -6, -2, -8, 2, -10, 4, -2, 8, -8, 6, 5, -2, -6, 1, -6, -10,
     3, 5, -7, -6, 9, 5, 10, 8, 8, -6, 8, -9, -6, 5, -7, -2, 1, -4, 1, -3, -1, -1, 4, 7, 5, -3, 3, 8, 10, 9, -3, -4, 0,
     -6, 9, 7, 6, -7, -7, 2, 6, -3, -4, 9, 10, -3, 4, 0, 0, 9, 9, 3, -9, 2, -1, 2, 3, 8, 6, -3, 8, -10, -5, 1, -8, 9, 3,
     7, 2, -5, 7, 8, 0, 3, 0, 9, 7, -4, -5, -1, -9, 2, 5, -3, -8, -9, 8, -4, 2, 2, -10, -7, 0, 5, 0, 2, 8, 7, 6, 6, 6,
     3, 8, -1, -2, -8, 5, 0, 2, -1, -4, -10, -9, -1, -9, 10, 5, -8, -7, -2, -9, 8, 5, 7, 4, 4, -8, 6, -5, 8, 10, -3, 2,
     -9, 9, -1, -4, -3, 2, 0, 3, -4, -5, 8, 9, -5, -4, 0, 0, 5, 6, 6, 5, -5, -5, 1, -1, -3, -8, -7, -2, -1, -1, 10, -4,
     -2, -9, 6, -3, 7, 1, 4, -5, 9, -4, 3, 6, 3, -9, 1, -5, 5, 7, -10, -6, 4, -6, -5, 9, 2, -9, 3, -9, -9, 0, 0, 3, -7,
     -1, -1, -4, 0, -9, 3, -8, 6, 9, 0, -10, -7, -2, -9, 5, -9, 10, 10, -6, 7, -2, -5, -7, -8, 9, 3, 6, 3, -3, -5, 7, 3,
     2, 5, 9, 7, -2, 1, 10, 6, 1, 4, -4, -6, 3, 3, 6, -2, 2, 8, 6, 2, 1, 8, -6, -4, 1, -9, 6, 5, 0, -3, 7, -1, -4, 6,
     -2, 7, 10, -4, -3, -10, -5, 1, 6, -5, 1, 5, -4, 8, 9, -7, 7, -8, 6, 3, -1, 4, -3, -8, -9, -3, -8, 8, -5, 6, -7, 5,
     0, -1, 0, -7, -4, 5, 7, 8, 10, -3, -3, -5, -3, 6, -6, -3, -2, 5, 2, 0, -1, -6, -6, -9, -10, 3, -6, -3, -9, 5, 10,
     -6, 3, 6, -1, 4, 1, -1, 5, 4, 0, -2, 8, 4, -7, -8, 10, -7, -4, -2, 2, 10, -7, -8, -10, 7, -9, -8, 4, 5, -9, -3, -7,
     3, 7, -10, -4, -8, 10, -6, 5, -6, -8, 8, -1, 1, -6, 10, -6, -1, -2, 6, -3, 3, -4, 9, 4, -4, 6, 8, 3, 10, -5, -1, 3,
     2, -2, -7, 4, -4, -2, -2, 3, 4, 0, -3, 2, 2, 0, -1, -1, -5, -10, -6, 10, 5, -9, -6, -5, 8, 10, 0, -10, -10, 6, 2,
     -4, -6, -3, 4, -10, 7, -9, -7, 2, 9, 2, 1, 4, -10, 10, -7, 5, -3, -4, -8, -6, 7, 10, 4, 10, 8, -8, 5, 1, 0, 8, -2,
     0, -9, 1, -3, 1, -1, -1, 5, -5, 5, -5, -4, -10, -7], 13))
print(s.maximumSubarraySum([1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7], 1))
print(s.maximumSubarraySum([1, 2, 3, 4, 5, 6, 2, 1, 2, 3, 4, 5], 1))
