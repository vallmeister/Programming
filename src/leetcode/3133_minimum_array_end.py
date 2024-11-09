class Solution:
    def minEnd(self, n: int, x: int) -> int:
        set_bits = x.bit_count()
        mask = 1 << 63
        result = x
        while n > 1:
            if x & mask > 0:
                set_bits -= 1
            candidates = mask >> set_bits
            if n - candidates > 0 and x & mask == 0:
                n -= candidates
                result |= mask
            mask >>= 1
        return result


s = Solution()
print(s.minEnd(3, 4))
print(s.minEnd(2, 7))
print(s.minEnd(4, 1))
print(s.minEnd(2, 4))
print(s.minEnd(2, 8))
print(s.minEnd(6715154, 7193485))
