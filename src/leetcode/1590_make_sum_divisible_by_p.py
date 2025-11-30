from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = ans = len(nums)
        target = sum(nums) % p
        if target == 0:
            return 0
        index_of_remainder = {0: -1}
        ps = 0
        for i, num in enumerate(nums):
            ps += num
            ps %= p
            r = (ps - target + p) % p
            if r in index_of_remainder:
                ans = min(ans, i - index_of_remainder[r])
            index_of_remainder[ps] = i
        return ans if ans < n else -1


s = Solution()
print(s.minSubarray(nums=[3, 1, 4, 2], p=6))
print(s.minSubarray(nums=[6, 3, 5, 2], p=9))
print(s.minSubarray(nums=[1, 2, 3], p=3))
print(s.minSubarray([26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3], 26))
print(s.minSubarray([1, 2, 3], 7))
