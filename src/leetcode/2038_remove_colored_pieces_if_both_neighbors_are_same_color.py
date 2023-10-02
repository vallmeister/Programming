from collections import deque


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        state = deque()
        n = len(colors)
        i = 0
        while i < n:
            curr_as = 0
            while i < n and colors[i] == 'A':
                curr_as += 1
                i += 1
            state.append(curr_as)
            curr_bs = 0
            while i < n and colors[i] == 'B':
                curr_bs += 1
                i += 1
            state.append(curr_bs)
        alice = 0
        bob = 0
        n = len(state)
        for i in range(n):
            if i % 2 == 0:
                alice += max(0, state[i] - 2)
            else:
                bob += max(0, state[i] - 2)
        return alice > bob

    def winner_of_game(self, colors):
        n = len(colors)
        alice = 0
        bob = 0
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bob += 1
        return alice > bob


s = Solution()
print(s.winnerOfGame("AAABABB"))
print(s.winnerOfGame('AA'))
print(s.winnerOfGame("ABBBBBBBAAA"))
