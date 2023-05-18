class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        for word_num in range(len(words)):
            for char_pos in range(len(words[word_num])):
                if char_pos >= len(words):
                    return False
                if len(words[char_pos]) <= word_num:
                    return False
                if words[word_num][char_pos] != words[char_pos][word_num]:
                    return False
        return True


s = Solution()
print(s.validWordSquare(["abcd", "bnrt", "crmy", "dtye"]))
print(s.validWordSquare(["abcd", "bnrt", "crm", "dt"]))
print(s.validWordSquare(["ball", "area", "read", "lady"]))
print(s.validWordSquare(["ball", "asee", "let", "lep"]))
print(s.validWordSquare(["abc", "b"]))
