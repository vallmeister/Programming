from collections import defaultdict


class Solution:
    def calculateScore(self, s: str) -> int:
        score = 0
        visited = defaultdict(list)
        for i, char in enumerate(s):
            mirror = self.get_mirror(char)
            if visited[mirror]:
                score += i - visited[mirror].pop()
            else:
                visited[char].append(i)
        return score

    def get_mirror(self, letter):
        offset = ord('a')
        value = ord(letter) - offset
        value = 25 - value
        value += offset
        return chr(value)


sol = Solution()
print(sol.calculateScore("aczzx"))
