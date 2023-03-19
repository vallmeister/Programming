class NumMatrix:
    block_sums = [[]]

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.block_sums = [[0] * n for _ in range(m)]
        for i in range(m):
            self.block_sums[i][0] = self.block_sums[i - 1][0] + matrix[i][0]
            row_sum = matrix[i][0]
            for j in range(1, n):
                row_sum += matrix[i][j]
                self.block_sums[i][j] = row_sum
                if i > 0:
                    self.block_sums[i][j] += self.block_sums[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.block_sums[row2][col2]
        if col1 > 0:
            result -= self.block_sums[row2][col1 - 1]
        if row1 > 0:
            result -= self.block_sums[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            result += self.block_sums[row1 - 1][col1 - 1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
obj = NumMatrix([[-1]])
print(obj.sumRegion(0, 0, 0, 0))
