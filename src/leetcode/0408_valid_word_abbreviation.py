class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        n = len(word)
        m = len(abbr)
        while i < n or j < m:
            if i < n and j < m and abbr[j].isalpha() and word[i] == abbr[j]:
                i += 1
                j += 1
            elif j < m and abbr[j].isdigit():
                start = j
                while j < m and abbr[j].isdigit():
                    j += 1
                num = int(abbr[start:j])
                if abbr[start] == '0':
                    return False
                i += num
            else:
                return False
        if i - n != j - m:
            return False
        return True


s = Solution()
print(s.validWordAbbreviation("internationalization", abbr="i12iz4n"))
print(s.validWordAbbreviation("apple", abbr="a2e"))
print(s.validWordAbbreviation("substitution", "s10n"))
print(s.validWordAbbreviation("substitution", "sub4u4"))
print(s.validWordAbbreviation("substitution", "12"))
print(s.validWordAbbreviation("substitution", "su3i1u2on"))
print(s.validWordAbbreviation("substitution", "substitution"))
print(s.validWordAbbreviation("substitution", "s55n"))
print(s.validWordAbbreviation("substitution", "s010n"))
print(s.validWordAbbreviation("substitution", "s0ubstitution"))
print(s.validWordAbbreviation('a', '2'))
print(s.validWordAbbreviation('hi', '1'))
