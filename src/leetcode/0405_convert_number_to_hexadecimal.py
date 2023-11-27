class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        dec_to_hex = {i: i for i in range(10)} | {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        negative = num < 0
        ans = []
        if negative:
            num += 1
            num = abs(num)
            for i in range(8):
                ans.append(str(dec_to_hex[15 - num % 16]))
                num //= 16
        else:
            while num > 0:
                ans.append(str(dec_to_hex[num % 16]))
                num //= 16
        return ''.join(ans[::-1])


s = Solution()
print(s.toHex(26))
print(s.toHex(-1))
print(s.toHex(-3))
