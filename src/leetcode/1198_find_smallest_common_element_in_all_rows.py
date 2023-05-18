class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        intersect = set(mat[0])
        for row in mat[1:]:
            intersect = intersect.intersection(set(row))
            if len(intersect) == 0:
                return -1
        return min(intersect)


s = Solution()
print(s.smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
print(s.smallestCommonElement([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
