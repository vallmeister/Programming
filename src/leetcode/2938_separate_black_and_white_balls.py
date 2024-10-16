class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        ans = 0
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            while i < j and s[i] == '0':
                i += 1
            while i < j and s[j] == '1':
                j -= 1
            if i < j:
                ans += j - i
                s[i], s[j] = s[j], s[i]
        return ans
