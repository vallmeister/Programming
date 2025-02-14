from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        cross_sums = [[-1] * 2 for _ in range(100)]
        for num in nums:
            cs = self.get_cross_sum(num)
            if num > cross_sums[cs][0]:
                cross_sums[cs][1] = cross_sums[cs][0]
                cross_sums[cs][0] = num
            elif num > cross_sums[cs][1]:
                cross_sums[cs][1] = num
        for fst, snd in cross_sums:
            if fst < 0 or snd < 0:
                continue
            ans = max(ans, fst + snd)
        return ans

    def get_cross_sum(self, n):
        cs = 0
        while n > 0:
            cs += n % 10
            n //= 10
        return cs
