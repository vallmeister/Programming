class Solution:
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        total_shift = 0
        for direction, amount in shift:
            if direction == 0:
                total_shift -= amount
            else:
                total_shift += amount
        right_shift = total_shift > 0
        total_shift = abs(total_shift)
        total_shift %= len(s)
        if total_shift == 0:
            return s
        if right_shift:
            return s[len(s) - total_shift:] + s[:len(s) - total_shift]
        else:
            return s[total_shift:] + s[:total_shift]


sol = Solution()
print(sol.stringShift('abc', [[0, 1], [1, 2]]))
print(sol.stringShift('abcdefg', [[1, 1], [1, 1], [0, 2], [1, 3]]))
