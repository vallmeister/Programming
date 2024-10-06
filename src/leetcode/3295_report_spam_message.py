from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        hits = 0
        for word in message:
            if word in bannedWords:
                hits += 1
            if hits >= 2:
                return True
        return False
