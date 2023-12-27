from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_len = m + n
        discarded = 0
        left_1, left_2 = 0, 0
        right_1, right_2 = m - 1, n - 1
        while left_1 <= right_1 or left_2 <= right_2:
            if total_len % 2 == 1 and discarded == total_len // 2:
                if left_1 < right_1 and left_2 < right_2:
                    return min(nums1[left_1], nums2[left_2])
                elif left_1 < right_1:
                    return nums1[left_1]
                elif left_2 < right_2:
                    return nums2[left_2]
        pass


s = Solution()
print(s.findMedianSortedArrays([1, 3], nums2=[2]))
print(s.findMedianSortedArrays([1, 2], nums2=[3, 4]))
print(s.findMedianSortedArrays([1, 3, 4, 6, 8, 11, 12], [1, 2, 5, 7, 13, 20]))
