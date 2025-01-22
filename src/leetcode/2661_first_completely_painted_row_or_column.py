from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [0] * m
        columns = [0] * n
        indices = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        for idx, num in enumerate(arr):
            i, j = indices[num]
            rows[i] += 1
            if rows[i] == n:
                return idx
            columns[j] += 1
            if columns[j] == m:
                return idx
        return -1


s = Solution()
print(s.firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
