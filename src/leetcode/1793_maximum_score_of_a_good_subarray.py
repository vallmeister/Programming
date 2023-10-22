import bisect
import math
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def solve(nums, k):
            left = [0] * k
            curr_min = math.inf
            for i in range(k - 1, -1, -1):
                curr_min = min(curr_min, nums[i])
                left[i] = curr_min

            right = []
            curr_min = math.inf
            for i in range(k, n):
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)

            max_score = -math.inf
            for j in range(k, n):
                curr_min = right[j - k]
                i = bisect.bisect_left(left, curr_min)
                max_score = max(max_score, curr_min * (j - i + 1))
            return max_score

        return max(solve(nums, k), solve(nums[::-1], n - k - 1))


s = Solution()
print(s.maximumScore([1, 4, 3, 7, 4, 5], k=3))
print(s.maximumScore([5, 5, 4, 5, 4, 1, 1, 1], k=0))
