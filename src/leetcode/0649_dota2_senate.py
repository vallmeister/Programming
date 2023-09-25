from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiants.append(i)
            elif senate[i] == 'D':
                dires.append(i)
        next_senator = 0
        while radiants or dires:
            if not radiants:
                return "Dire"
            if not dires:
                return "Radiant"
            if next_senator == radiants[0]:
                nxt = radiants.popleft()
                dires.popleft()
                radiants.append(nxt)
            elif next_senator == dires[0]:
                nxt = dires.popleft()
                radiants.popleft()
                dires.append(nxt)
            next_senator += 1
            next_senator %= len(senate)
        return ""


s = Solution()
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))
