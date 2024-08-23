class Solution:
    def findComplement(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 2)
            num //= 2
        for i in range(len(digits)):
            digits[i] = 1 - digits[i]
        base = 1
        ans = 0
        for d in digits:
            ans += d * base
            base *= 2
        return ans
