class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        complement = []
        while n > 0:
            complement.append(n % 2)
            n //= 2
        for i in range(len(complement)):
            complement[i] = 1 - complement[i]
        ans = 0
        base = 1
        for digit in complement:
            ans += digit * base
            base *= 2
        return ans

    def bitwise_complement_optimized(self, n):
        if n == 0:
            return 1
        todo = n
        bit = 1
        while todo:
            n = n ^ bit
            todo >>= 1
            bit <<= 1
        return n


s = Solution()
print(s.bitwiseComplement(5))
print(s.bitwiseComplement(7))
print(s.bitwiseComplement(10))
