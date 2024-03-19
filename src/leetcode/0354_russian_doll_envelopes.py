import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for num in nums:
                ip = bisect.bisect_left(dp, num)
                if ip == len(dp):
                    dp.append(num)
                else:
                    dp[ip] = num
            return len(dp)

        return lis([i[1] for i in envelopes])
