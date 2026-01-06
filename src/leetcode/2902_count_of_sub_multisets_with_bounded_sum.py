from collections import Counter
from typing import List


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        num_counter = Counter(nums)
        zeroes = num_counter[0]
        del num_counter[0]
        dp = [1] + [0] * r
        for num, count in sorted(num_counter.items()):
            stride_sums = dp[:]
            # we add more to our sums than count would actually allow
            for i in range(num, r + 1):
                stride_sums[i] += stride_sums[i - num]
            for i in reversed(range(r + 1)):
                # we update dp, because we added everything in stride sums, so we do not add again
                dp[i] = stride_sums[i]
                # we now have to subtract the values that are more than count would have allowed
                if i >= num * (count + 1):
                    dp[i] -= stride_sums[i - num * (count + 1)]
        ans = 0
        for i in range(l, r + 1):
            ans += dp[i] * (zeroes + 1)
            ans %= MOD
        return ans


s = Solution()
print(s.countSubMultisets(nums=[1, 2, 2, 3], l=6, r=6))
print(s.countSubMultisets(nums=[2, 1, 4, 2, 7], l=1, r=5))
print(s.countSubMultisets(nums=[1, 2, 1, 3, 5, 2], l=3, r=5))
print(s.countSubMultisets([0, 0, 1, 2, 3], 2, 3))  # 9
