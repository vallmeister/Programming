class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0
        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1
        for j in range(i - 1, -1, -1):
            char = s[j]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return s[j]
                length -= 1
        return s[0]


sol = Solution()
print(sol.decodeAtIndex("leet2code3", k=10))
print(sol.decodeAtIndex("ha22", k=5))
print(sol.decodeAtIndex("a2345678999999999999999", k=1))
