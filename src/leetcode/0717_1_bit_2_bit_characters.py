from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n:
            if i == n - 1 and bits[i] == 0:
                return True
            elif bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        return False
