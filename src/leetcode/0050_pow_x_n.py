class Solution:
    def myPow(self, x: float, n: int) -> float:

        def my_pow_recursive(b, e):
            if e == 0:
                return 1
            elif e % 2 == 0:
                return my_pow_recursive(b * b, e / 2)
            else:
                return b * my_pow_recursive(b * b, e // 2)

        if n < 0:
            return 1.0 / my_pow_recursive(x, -n)
        else:
            return my_pow_recursive(x, n)

    def my_pow_iterative(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1.0 / x
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            x *= x
            n /= 2
        return result


s = Solution()
print(s.myPow(2.0, 10))
print(s.myPow(2.1, 3))
print(s.myPow(2.0, -2))
print(s.myPow(0.00001, 2147483647))
