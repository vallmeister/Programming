class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        curr_min = mat[0][0]
        pointers = [0] * m
        while True:
            for i in range(m):
                j = pointers[i]
                while j < n and mat[i][j] < curr_min:
                    j += 1
                if j == n:
                    return -1
                elif curr_min < mat[i][j]:
                    curr_min = mat[i][j]
                    break
            else:
                return curr_min


s = Solution()
print(s.smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
print(s.smallestCommonElement([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
print(s.smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 4, 7, 9, 11], [1, 3, 5, 7, 9]]))
