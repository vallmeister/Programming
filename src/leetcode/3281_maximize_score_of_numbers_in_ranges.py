from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        left = 0
        right = start[-1] + d
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            curr = start[0]
            for num in start[1:]:
                if curr + mid > num + d:
                    right = mid - 1
                    break
                else:
                    curr = max(curr + mid, num)
            else:
                ans = max(ans, mid)
                left = mid + 1
        return ans
