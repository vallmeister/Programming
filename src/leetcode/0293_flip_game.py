from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        ans = []
        currentState = list(currentState)
        for i in range(n - 1):
            if currentState[i] == currentState[i + 1] == '+':
                currentState[i] = '-'
                currentState[i + 1] = '-'
                ans.append(''.join(currentState))
                currentState[i] = '+'
                currentState[i + 1] = '+'
        return ans
