class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                ones += 1
            mask <<= 1
        return ones
