class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = num1.bit_count()
        b2 = num2.bit_count()
        if b1 > b2:
            n = num1
            for _ in range(b1 - b2):
                lsb = n & (-n)
                n ^= lsb
            ans = 0
            for _ in range(b2):
                lsb = n & (-n)
                n ^= lsb
                ans |= lsb
            return ans
        elif b1 == b2:
            return num1
        else:
            mask = 1
            ans = num1
            while b2 - b1 > 0:
                if mask & num1 == 0:
                    ans |= mask
                    b2 -= 1
                mask <<= 1
            return ans


s = Solution()
print(s.minimizeXor(1, 12))
