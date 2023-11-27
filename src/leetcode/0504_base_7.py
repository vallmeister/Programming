class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = num < 0
        num = abs(num)
        ans = []
        while num > 0:
            ans.append(str(num % 7))
            num //= 7
        if sign:
            ans.append('-')
        return ''.join(ans[::-1])


s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))
