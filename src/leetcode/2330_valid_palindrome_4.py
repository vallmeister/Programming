class Solution:
    def makePalindrome(self, s: str) -> bool:
        mismatches = 0
        i = 0
        j = len(s) - 1
        while i < j and mismatches <= 2:
            if s[i] != s[j]:
                mismatches += 1
            i += 1
            j -= 1
        return mismatches <= 2


sol = Solution()
print(sol.makePalindrome("abcdba"))
print(sol.makePalindrome("aa"))
print(sol.makePalindrome("abcdef"))
