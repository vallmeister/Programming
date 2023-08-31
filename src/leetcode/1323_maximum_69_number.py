class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == '6':
                return int(num[:i] + '9' + num[i + 1:])
        return int(num)


s = Solution()
print(s.maximum69Number(9669))
print(s.maximum69Number(9996))
print(s.maximum69Number(9996))
print(s.maximum69Number(9999))
