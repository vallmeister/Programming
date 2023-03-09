class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = ''
        if num < 0:
            sign = '-'
            num = -num
        base7 = ''
        while num > 0:
            base7 += str(num % 7)
            num //= 7
        return sign + base7[::-1]


s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))
