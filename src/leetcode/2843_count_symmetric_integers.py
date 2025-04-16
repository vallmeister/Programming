class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            n = len(str(i))
            if n % 2 == 1:
                continue
            right = self.get_sum_of_last_n_digits(i, n // 2)
            i //= 10 ** (n // 2)
            left = self.get_sum_of_last_n_digits(i, n // 2)
            if right == left:
                ans += 1

        return ans

    def get_sum_of_last_n_digits(self, num, n):
        ans = 0
        for _ in range(n):
            ans += num % 10
            num //= 10
        return ans

s = Solution()
print(s.countSymmetricIntegers(1, 100))
print(s.countSymmetricIntegers(1200, 1230))
