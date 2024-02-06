from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            counter = tuple(counter)
            if counter in h:
                h[counter].append(s)
            else:
                h[counter] = [s]
        return [group for group in h.values()]
