from collections import deque


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = deque(sentence1.split())
        sentence2 = deque(sentence2.split())
        while sentence1 and sentence2 and sentence1[0] == sentence2[0]:
            sentence1.popleft()
            sentence2.popleft()
        while sentence1 and sentence2 and sentence1[-1] == sentence2[-1]:
            sentence1.pop()
            sentence2.pop()
        return not sentence1 or not sentence2


s = Solution()
print(s.areSentencesSimilar(sentence1="My name is Haley", sentence2="My Haley"))
print(s.areSentencesSimilar("c h p Ny", "c BDQ r h p Ny"))
