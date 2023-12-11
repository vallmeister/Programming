from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) / 4
        curr = arr[0]
        count = 1
        for num in arr[1:]:
            if count > threshold:
                return curr
            elif curr == num:
                count += 1
            else:
                curr = num
                count = 1
        return curr


s = Solution()
print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(s.findSpecialInteger([1, 1]))
print(s.findSpecialInteger([1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12]))
print(s.findSpecialInteger([1, 2, 3, 3]))
