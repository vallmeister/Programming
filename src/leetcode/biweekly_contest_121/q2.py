from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tmp = 0
        for num in nums:
            tmp ^= num
        ans = 0
        while k > 0 or tmp > 0:
            ans += (tmp ^ k) & 1
            tmp= tmp >> 1
            k = k >> 1
        return ans


s = Solution()
print(s.minOperations([2, 1, 3, 4], k=1))
print(s.minOperations([2, 0, 2, 0], k=0))
