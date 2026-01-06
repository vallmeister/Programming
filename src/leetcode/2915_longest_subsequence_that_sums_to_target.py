import math
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = [[-1] * (target + 1) for _ in range(n)]

        def memo(i, remaining):
            if i >= n:
                if remaining == 0:
                    return 0
                else:
                    return -math.inf
            elif remaining < 0:
                return -math.inf
            elif cache[i][remaining] != -1:
                return cache[i][remaining]
            take = 1 + memo(i + 1, remaining - nums[i])
            no_take = memo(i + 1, remaining)
            cache[i][remaining] = max(take, no_take)
            return cache[i][remaining]

        return max(memo(0, target), -1)


s = Solution()
print(s.lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3))
