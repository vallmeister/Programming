class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        last_char = word[0]

        def almost_equal(a, b):
            return abs(ord(a) - ord(b)) <= 1

        for char in word[1:]:
            if last_char == '*':
                last_char = char
            elif almost_equal(last_char, char):
                ans += 1
                last_char = '*'
            else:
                last_char = char
        return ans


s = Solution()
print(s.removeAlmostEqualCharacters("aaaaa"))
print(s.removeAlmostEqualCharacters("abddez"))
print(s.removeAlmostEqualCharacters("zyxyxyz"))
print(s.removeAlmostEqualCharacters('aca'))
