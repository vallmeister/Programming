from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        ransomNote = Counter(ransomNote)
        for letter, number in ransomNote.items():
            if magazine[letter] < number:
                return False
        return True


s = Solution()
print(s.canConstruct("a", magazine="b"))
print(s.canConstruct("aa", magazine="ab"))
print(s.canConstruct("aa", magazine="aab"))
