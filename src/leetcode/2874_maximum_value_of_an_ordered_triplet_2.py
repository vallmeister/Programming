from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * (n + 1)
        for i in range(1, n + 1):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
        right_max = [0] * (n + 1)
        for i in reversed(range(n - 1)):
            right_max[i] = max(right_max[i + 1], nums[i + 1])

        ans = 0
        for j in range(n):
            i = left_max[j]
            k = right_max[j]
            ans = max(ans, (i - nums[j]) * k)
        return ans


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))
print(s.maximumTripletValue([1, 2, 3]))
