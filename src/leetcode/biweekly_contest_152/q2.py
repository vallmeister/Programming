class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.get_row_and_col(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        formula = formula.replace('=', '')
        x, y = formula.split('+')
        if x.isnumeric():
            x = int(x)
        else:
            row, col = self.get_row_and_col(x)
            x = self.grid[row][col]
        if y.isnumeric():
            y = int(y)
        else:
            row, col = self.get_row_and_col(y)
            y = self.grid[row][col]
        return x + y

    def get_row_and_col(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        return row, col


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)©leetcode

s = Spreadsheet(3)
print(s.getValue('=5+7'))
print(s.setCell("A1", 10))
print(s.getValue("=A1+6"))
