class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = max(query_row, query_glass)
        tower = [[0.0] * (n + 1) for _ in range(n + 1)]
        tower[0][0] = float(poured)
        for i in range(n):
            for j in range(n):
                if tower[i][j] > 1.0:
                    overflow = tower[i][j] - 1.0
                    tower[i + 1][j] += overflow / 2
                    tower[i + 1][j + 1] += overflow / 2

        return min(tower[query_row][query_glass], 1.0)


s = Solution()
print(s.champagneTower(1, 1, 1))
print(s.champagneTower(2, 1, 1))
print(s.champagneTower(100000009, query_row=33, query_glass=17))
