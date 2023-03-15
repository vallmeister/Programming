class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif len(s) == 2 and int(s) <= 26:
            return 1
        res = 1
        for i in range(1, len(s)):
            if s[i] == '0' and i >= 1 and not (s[i - 1] == '1' or s[i - 1] == '2'):
                return 0
            elif s[i] == '0':
                res -= 1
            else:
                if int(s[i - 1: i + 1]) <= 26 and int(s[i - 1]) != 0:
                    res += 1
        return res


s = Solution()
print(s.numDecodings('12'))
print(s.numDecodings('226'))
print(s.numDecodings('06'))
print(s.numDecodings('2101'))
print(s.numDecodings('10'))
