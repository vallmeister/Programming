class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        for row in range(m):
            left = 0
            right = n - 1
            rightmost_soldier = -1
            while left <= right:
                mid = (left + right) // 2
                if mat[row][mid] == 1:
                    rightmost_soldier = max(rightmost_soldier, mid)
                    left = mid + 1
                elif mat[row][mid] == 0:
                    right = mid - 1
            res.append((row, rightmost_soldier + 1))

        return [y[0] for y in sorted(res, key=lambda x: (x[1], x[0]))][:k]


s = Solution()
print(s.kWeakestRows([[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]], 3))
print(s.kWeakestRows([[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]], 2))
