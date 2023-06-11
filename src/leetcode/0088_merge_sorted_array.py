from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            elif nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[i], nums1[k] = nums1[k], nums1[i]
                i -= 1
                k -= 1


s = Solution()
arr = [1, 2, 3, 0, 0, 0]
s.merge(arr, m=3, nums2=[2, 5, 6], n=3)
print(arr)
arr = [1]
s.merge(arr, m=1, nums2=[], n=0)
print(arr)
arr = [0]
s.merge(arr, m=0, nums2=[1], n=1)
print(arr)
arr = [0, 0, 0, 0, 0]
s.merge(arr, 0, [1, 2, 3, 4, 5], 5)
print(arr)
arr = [4, 0, 0, 0, 0, 0]
s.merge(arr, 1, [1, 2, 3, 5, 6], 5)
print(arr)
