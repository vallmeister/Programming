class Solution:
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        n = len(s)
        total = 0
        for direction, amount in shift:
            total += (-1) ** direction * amount
        total %= n
        return s[total:] + s[:total]


sol = Solution()
print(sol.stringShift('abc', [[0, 1], [1, 2]]))
print(sol.stringShift('abcdefg', [[1, 1], [1, 1], [0, 2], [1, 3]]))
