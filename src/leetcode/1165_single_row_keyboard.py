class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = {k: v for k, v in zip(keyboard, range(len(keyboard)))}
        t = pos = 0
        for c in word:
            idx = keyboard[c]
            t += abs(idx - pos)
            pos = idx
        return t


s = Solution()
print(s.calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba"))
print(s.calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode"))
