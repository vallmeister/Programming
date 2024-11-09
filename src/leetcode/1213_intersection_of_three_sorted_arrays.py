from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)
        i = j = k = 0
        res = []
        while i < n1 and j < n2 and k < n3:
            curr_num = max(arr1[i], arr2[j], arr3[k])
            while i < n1 and arr1[i] < curr_num:
                i += 1
            while j < n2 and arr2[j] < curr_num:
                j += 1
            while k < n3 and arr3[k] < curr_num:
                k += 1
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
        return res
