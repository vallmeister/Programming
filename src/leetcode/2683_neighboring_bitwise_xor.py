from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if n == 1:
            return derived[0] == 0
        original = [0] * n
        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]
        return original[0] ^ original[n - 1] == derived[n - 1]
