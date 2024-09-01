from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = []
        for i in range(m):
            curr_row = []
            for j in range(n):
                idx = i * n + j
                curr_row.append(original[idx])
            ans.append(curr_row)
        return ans
