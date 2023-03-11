class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        dec_to_hex = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        for i in range(10):
            dec_to_hex[i] = i
        answer = ''
        if num < 0:
            num = 2 ** 32 + num
        while num > 0:
            answer += str(dec_to_hex[num % 16])
            num //= 16
        return answer[::-1]


s = Solution()
print(s.toHex(26))
print(s.toHex(-1))
