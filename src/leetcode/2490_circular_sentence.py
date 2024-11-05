class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        prev = sentence[0]
        for word in sentence[1:]:
            if prev[-1] != word[0]:
                return False
            prev = word
        return sentence[0][0] == sentence[-1][-1]
