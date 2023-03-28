class Solution:
    def rshift(self, val, n):
        return (val % 0x100000000) >> n

    def getSum(self, a: int, b: int) -> int:
        carry = 0
        result = 0
        power = 0
        while a or b or carry:
            a_i = a & 1
            b_i = b & 1
            digit = a_i ^ b_i ^ carry
            result |= digit << power
            power += 1
            carry = a_i & b_i | a_i & carry | b_i & carry
            a = self.rshift(a, 1)
            b = self.rshift(b, 1)
        return result


s = Solution()
print(s.getSum(1, 2))
print(s.getSum(2, 3))
print(s.getSum(2, -3))
print(s.getSum(20, 30))
