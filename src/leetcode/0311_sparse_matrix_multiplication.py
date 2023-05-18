class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])
        sparse_rows = set()
        sparse_columns = set()
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    break
            else:
                sparse_rows.add(i)
        for i in range(n):
            for j in range(k):
                if mat2[j][i] != 0:
                    break
            else:
                sparse_columns.add(i)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i in sparse_rows or j in sparse_columns:
                    continue
                for h in range(k):
                    res[i][j] += mat1[i][h] * mat2[h][j]
        return res


s = Solution()
print(s.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(s.multiply([[0]], [[0]]))
