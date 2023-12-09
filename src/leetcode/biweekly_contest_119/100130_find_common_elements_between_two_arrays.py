from collections import Counter
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        left = 0
        for num, occurrence in nums1.items():
            if num in nums2:
                left += occurrence
        right = 0
        for num, occurrence in nums2.items():
            if num in nums1:
                right += occurrence
        return [left, right]


s = Solution()
print(s.findIntersectionValues([4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
print(s.findIntersectionValues([3, 4, 2, 3], nums2=[1, 5]))
