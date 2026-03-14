class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        count = r - l + 1  # number of different digits
        digit_sum = (count * (l + r) // 2)  # sum of these digits
        appearances_per_position = pow(count, k - 1, MOD)  # how often every digit appears at each position

        # shifting the result by multiplying with 1111...1 = (10^k - 1) // 9
        pow10 = pow(10, k, MOD)
        inv9 = pow(9, MOD - 2, MOD)  # follows from Fermat's little theorem since we use modulo arithmetic
        positional_weights = ((pow10 - 1) * inv9) % MOD

        return (digit_sum * appearances_per_position * positional_weights) % MOD


s = Solution()
print(s.sumOfNumbers(l=1, r=2, k=2))
print(s.sumOfNumbers(l=0, r=1, k=3))
print(s.sumOfNumbers(l=5, r=5, k=10))
