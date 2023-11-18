from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > 2 * nums[i]:
                    break
                ans = max(ans, nums[i] ^ nums[j])

        return ans


s = Solution()
print(s.maximumStrongPairXor([1, 2, 3, 4, 5]))
print(s.maximumStrongPairXor([10, 100]))
print(s.maximumStrongPairXor([5, 6, 25, 30]))
