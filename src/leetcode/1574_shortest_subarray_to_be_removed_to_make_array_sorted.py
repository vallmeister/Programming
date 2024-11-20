import bisect
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        ans = right
        for left in range(n):
            if left > 0 and arr[left - 1] > arr[left] or left >= right:
                break
            while right < n and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
        return ans


s = Solution()
print(s.findLengthOfShortestSubarray([13, 0, 14, 7, 18, 18, 18, 16, 8, 15, 20]))
print(s.findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1]))
