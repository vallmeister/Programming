from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in reversed(range(n)):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry > 0:
            digits = [carry] + digits
        return digits
