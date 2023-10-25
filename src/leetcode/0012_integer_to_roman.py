class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_symbol = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL',
                         90: 'XC', 400: 'CD', 900: 'CM'}
        ans = []
        for i in range(4, -1, -1):
            base = 10 ** i
            leading_digit = num // base
            if leading_digit * base in num_to_symbol:
                ans.append(num_to_symbol[leading_digit * base])
            elif leading_digit > 5:
                ans.append(num_to_symbol[5 * base])
                for j in range(leading_digit - 5):
                    ans.append(num_to_symbol[base])
            elif leading_digit > 0:
                for j in range(leading_digit):
                    ans.append(num_to_symbol[base])

            num -= leading_digit * base

        return ''.join(ans)


s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
