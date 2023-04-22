class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        visited = set()
        for num in arr:
            if num / 2 in visited or num * 2 in visited:
                return True
            visited.add(num)
        return False


s = Solution()
print(s.checkIfExist([10, 2, 5, 3]))
print(s.checkIfExist([3, 1, 7, 11]))
