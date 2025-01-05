from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        offset = ord('a')
        letters = [ord(letter) - offset for letter in s]
        shift_start = [0] * n
        shift_end = [0] * n
        for start, end, direction in shifts:
            shift = (-1) ** (1 - direction)
            shift_start[start] += shift
            shift_end[end] -= shift
        total = 0
        for i in range(n):
            total += shift_start[i]
            letters[i] = chr(((letters[i] + total) % 26) + offset)
            total += shift_end[i]

        return ''.join(letters)


sol = Solution()
print(sol.shiftingLetters("abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
print(sol.shiftingLetters("dztz", shifts=[[0, 0, 0], [1, 1, 1]]))
