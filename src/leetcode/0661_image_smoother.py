from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                cells = 1
                val = img[row][col]
                if row > 0 and col > 0:
                    val += img[row - 1][col - 1]
                    cells += 1
                if row > 0:
                    val += img[row - 1][col]
                    cells += 1
                if row > 0 and col < n - 1:
                    val += img[row - 1][col + 1]
                    cells += 1
                if col > 0:
                    val += img[row][col - 1]
                    cells += 1
                if col < n - 1:
                    val += img[row][col + 1]
                    cells += 1
                if row < m - 1 and col > 0:
                    val += img[row + 1][col - 1]
                    cells += 1
                if row < m - 1:
                    val += img[row + 1][col]
                    cells += 1
                if row < m - 1 and col < n - 1:
                    val += img[row + 1][col + 1]
                    cells += 1
                ans[row][col] = val // cells
        return ans


s = Solution()
print(s.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
