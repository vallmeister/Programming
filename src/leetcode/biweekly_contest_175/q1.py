class Solution:
    def reverseByType(self, s: str) -> str:
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        s = list(s)
        normal = []
        special = []
        for c in s:
            if c in lowercase:
                normal.append(c)
            else:
                special.append(c)
        for i in range(len(s)):
            if s[i] in lowercase:
                s[i] = normal.pop()
            else:
                s[i] = special.pop()
        return ''.join(s)
