class Solution:
    def reverseBits(self, n: int) -> int:
        rev_n = 0
        power = 31
        while n:
            rev_n |= (n & 1) << power
            n >>= 1
            power -= 1
        return rev_n

    def reverse_bits_divide_and_conquer(self, n):

        def reverse_bits(number, bits):
            if bits == 1:
                return number
            bits //= 2
            # mask
            mask_right = (1 << bits) - 1
            mask_left = mask_right << bits
            right_bits = number & mask_right
            left_bits = number & mask_left
            # shift
            left_bits >>= bits
            left_bits &= mask_right
            right_bits <<= bits
            # combine
            return reverse_bits(right_bits, bits) | reverse_bits(left_bits, bits)

        return reverse_bits(n, 32)

s = Solution()
print(s.reverseBits(43261596))
print(s.reverse_bits_divide_and_conquer(43261596))
