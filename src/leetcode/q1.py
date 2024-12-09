class Solution:
    def smallestNumber(self, n: int) -> int:
        req = n.bit_length()
        while n.bit_count() != req:
            n += 1
        return n
