import math
from collections import Counter
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        outlier = -math.inf
        total = sum(nums)
        counter = Counter(nums)
        for candidate in nums:
            if candidate < outlier or (total - candidate) % 2 == 1:
                continue
            counter[candidate] -= 1
            if counter[candidate] == 0:
                del counter[candidate]
            curr_total = total - candidate
            curr_total //= 2
            if curr_total in counter:
                outlier = max(outlier, candidate)
            counter[candidate] += 1
        return outlier


s = Solution()
print(s.getLargestOutlier([-708, -708, 286]))
