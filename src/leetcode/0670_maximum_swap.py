class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        digits = self.get_digits(num)
        n = len(digits)
        max_digit = [-1] * n
        max_idx = [-1] * n
        for i in range(n):
            if digits[i] > max_digit[i - 1]:
                max_digit[i] = digits[i]
                max_idx[i] = i
            else:
                max_digit[i] = max_digit[i - 1]
                max_idx[i] = max_idx[i - 1]
        for i in reversed(range(1, n)):
            if digits[i] < max_digit[i - 1]:
                digits[i], digits[max_idx[i - 1]] = digits[max_idx[i - 1]], digits[i]
                num = max(num, self.get_num(digits))
                digits[i], digits[max_idx[i - 1]] = digits[max_idx[i - 1]], digits[i]
        return num

    def get_digits(self, num):
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        return digits

    def get_num(self, digits):
        num = 0
        for i, digit in enumerate(digits):
            num += digit * 10 ** i
        return num
