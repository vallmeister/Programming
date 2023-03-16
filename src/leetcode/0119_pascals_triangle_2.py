class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            new_row = [1]
            for j in range(1, i):
                new_row.append(row[j - 1] + row[j])
            new_row.append(1)
            row = new_row
        return row


s = Solution()
print(s.getRow(3))
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(4))
