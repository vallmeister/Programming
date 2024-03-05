class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            char = s[i]
            while i <= j and s[i] == char:
                i += 1
            while i <= j and s[j] == char:
                j -= 1
        return j - i + 1


print(Solution().minimumLength("bbbbbbbbbbbbbbbbbbb"))
