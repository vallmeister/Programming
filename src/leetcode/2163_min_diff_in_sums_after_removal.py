import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        curr_nums = []
        curr_sum = 0
        for num in nums[:n]:
            heappush(curr_nums, -num)
            curr_sum += num

        min_sum_left = [curr_sum]
        for i in range(n, 2 * n):
            num = nums[i]
            curr_sum += num
            heappush(curr_nums, -num)
            curr_sum += heappop(curr_nums)
            min_sum_left.append(min(min_sum_left[-1], curr_sum))

        curr_nums = []
        curr_sum = 0
        for num in nums[-n:]:
            heappush(curr_nums, num)
            curr_sum += num

        max_sum_right = [curr_sum]
        for i in reversed(range(n, 2 * n)):
            num = nums[i]
            curr_sum += num
            heappush(curr_nums, num)
            curr_sum -= heappop(curr_nums)
            max_sum_right.append(max(max_sum_right[-1], curr_sum))

        ans = math.inf
        for i in range(n + 1):
            ans = min(ans, min_sum_left[i] - max_sum_right[n - i])
        return ans


s = Solution()
print(s.minimumDifference([3, 1, 2]))
print(s.minimumDifference([7, 9, 5, 8, 1, 3]))
