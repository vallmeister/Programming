from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        return sum(n1 * n2 for n1, n2 in zip(nums1, nums2))


s = Solution()
print(s.minProductSum([5, 3, 4, 2], nums2=[4, 2, 2, 5]))
print(s.minProductSum([2, 1, 4, 5, 7], nums2=[3, 2, 4, 8, 6]))
