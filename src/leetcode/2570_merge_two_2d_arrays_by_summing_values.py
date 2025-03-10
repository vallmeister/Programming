from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        ans = []
        while i < m and j < n:
            id1, num1 = nums1[i]
            id2, num2 = nums2[j]
            if id1 == id2:
                ans.append([id1, num1 + num2])
                i += 1
                j += 1
            elif id1 < id2:
                ans.append([id1, num1])
                i += 1
            elif id1 > id2:
                ans.append([id2, num2])
                j += 1
        while i < m:
            ans.append(nums1[i])
            i += 1
        while j < n:
            ans.append(nums2[j])
            j += 1
        return ans
