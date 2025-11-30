from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        line_sweep = [0] * (length + 1)
        for start, end, inc in updates:
            line_sweep[start] += inc
            line_sweep[end + 1] -= inc
        curr = 0
        for i in range(length):
            curr += line_sweep[i]
            ans[i] = curr
        return ans
