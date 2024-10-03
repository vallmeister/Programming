from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = 0
        for i in range(n):
            target = (target + nums[i]) % p
        if target == 0:
            return 0
        ans = n
        curr_sum = 0
        prev_idx = {0: -1}
        for i in range(n):
            curr_sum = (curr_sum + nums[i]) % p
            val = (curr_sum - target + p) % p
            if val in prev_idx:
                ans = min(ans, i - prev_idx[val])
            prev_idx[curr_sum] = i
        return ans if ans < n else -1


s = Solution()
print(s.minSubarray([26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3], 26))
