class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        for i in range(1, len(s) // 2 + 1):
            substring = s[:i]
            for j in range(1, len(s) // len(substring) + 1):
                if substring * j == s:
                    return True
        return False


sol = Solution()
print(sol.repeatedSubstringPattern('abab'))
print(sol.repeatedSubstringPattern('aba'))
print(sol.repeatedSubstringPattern('abcabcabcabc'))
print(sol.repeatedSubstringPattern('a'))
print(sol.repeatedSubstringPattern('bb'))
