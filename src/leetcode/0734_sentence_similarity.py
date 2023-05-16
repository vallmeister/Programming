from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        synonyms = defaultdict(set)
        if len(sentence1) != len(sentence2):
            return False
        for k, v in similarPairs:
            synonyms[k].add(v)
            synonyms[v].add(k)
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in synonyms[sentence1[i]]:
                continue
            return False
        return True


s = Solution()
print(s.areSentencesSimilar(sentence1=["great", "acting", "skills"], sentence2=["fine", "drama", "talent"],
                            similarPairs=[["great", "fine"], ["drama", "acting"], ["skills", "talent"]]))
print(s.areSentencesSimilar(sentence1=["great"], sentence2=["great"], similarPairs=[]))
print(s.areSentencesSimilar(sentence1=["great"], sentence2=["doubleplus", "good"],
                            similarPairs=[["great", "doubleplus"]]))
print(s.areSentencesSimilar(["an", "extraordinary", "meal"], ["one", "good", "dinner"]
                            , [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"],
                               ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"],
                               ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"],
                               ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"],
                               ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"],
                               ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"],
                               ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"],
                               ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"],
                               ["actually", "very"], ["really", "very"], ["super", "very"]]
                            ))
