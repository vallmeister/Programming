class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:

        def dimensions(self) -> list[int]:
            pass
        pass

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        rows, cols = binaryMatrix.dimensions()

        def binary_search(curr_row):
            left, right = 0, cols - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if binaryMatrix.get(curr_row, mid):
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return idx

        left_most = 101
        for i in range(rows):
            j = binary_search(i)
            if j > -1:
                left_most = min(left_most, j)
        return left_most if left_most < 101 else -1
