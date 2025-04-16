class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (self.mod_exp(5, n // 2 + n % 2, mod) * self.mod_exp(4, n // 2, mod)) % mod

    def mod_exp(self, base, exp, mod):
        if exp == 0:
            return 1
        elif exp % 2 == 1:
            return (base * self.mod_exp(base, exp - 1, mod)) % mod
        base *= base
        base %= mod
        exp //= 2
        return self.mod_exp(base, exp, mod)


s = Solution()
print(s.countGoodNumbers(1))
print(s.countGoodNumbers(4))
print(s.countGoodNumbers(50))
print(s.countGoodNumbers(int(1e50)))
