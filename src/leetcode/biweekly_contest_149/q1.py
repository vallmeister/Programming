from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)
        for i in range(1, n):
            fst = s[i - 1]
            snd = s[i]
            if fst != snd and int(fst) == counter[fst] and int(snd) == counter[snd]:
                return fst + snd
        return ''
