from math import ceil, log2

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if k == 1:
            return 'a'
        while ceil(log2(k)) < len(operations):
            operations.pop()
        op = operations.pop()
        char = self.kthCharacter(k - 2 ** len(operations), operations)
        char = chr(((ord(char) - ord('a') + op) % 26) + ord('a'))
        return char


s = Solution()
print(s.kthCharacter(5, [0, 0, 0]))
print(s.kthCharacter(10, operations=[0, 1, 0, 1]))
