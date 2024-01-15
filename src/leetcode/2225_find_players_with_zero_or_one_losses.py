from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        loses = defaultdict(int)
        players = set()
        for winner, loser in matches:
            wins[winner] += 1
            loses[loser] += 1
            players.add(winner)
            players.add(loser)
        zero = sorted(player for player in players if loses[player] == 0)
        one = sorted(player for player in players if loses[player] == 1)
        return [zero, one]


s = Solution()
print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print(s.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
