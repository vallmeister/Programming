from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        ps = [0] * n
        for i in range(1, n):
            ps[i] = ps[i - 1] + 1 - ((nums[i] - nums[i - 1]) % 2)
        ans = []
        for left, right in queries:
            ans.append(ps[right] - ps[left] == 0)
        return ans


s = Solution()
print(s.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
