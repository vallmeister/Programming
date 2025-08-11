class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = set()
        mask = 1
        while mask <= 10 ** 9:
            powers.add(str(sorted(str(mask))))
            mask <<= 1
        return str(sorted(str(n))) in powers
