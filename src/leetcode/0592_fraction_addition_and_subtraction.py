import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        curr_numerator = 0
        curr_denominator = 1
        fractions = re.split('[+-]', expression)

        def get_operations():
            yield from (c for c in expression if c in ['+', '-'])
            yield '+'

        operations = get_operations()
        curr_operation = '+'
        for frac in fractions:
            if frac == '':
                curr_operation = next(operations)
                continue
            numerator, denominator = frac.split('/')
            numerator, denominator = int(numerator), int(denominator)
            if curr_denominator != denominator:
                tmp = curr_denominator
                curr_numerator *= denominator
                curr_denominator *= denominator
                numerator *= tmp
                denominator *= tmp
            if curr_operation == '+':
                curr_numerator += numerator
            elif curr_operation == '-':
                curr_numerator -= numerator
            gcd = self.gcd(curr_numerator, curr_denominator)
            curr_numerator //= gcd
            curr_denominator //= gcd
            curr_operation = next(operations)

        return str(curr_numerator) + '/' + str(curr_denominator)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


s = Solution()
print(s.fractionAddition("-1/2+1/2"))
print(s.fractionAddition("-1/2+1/2+1/3"))
print(s.fractionAddition("1/3-1/2"))
