from typing import List


class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        moves = 0
        rooks.sort()
        for i, pos in enumerate(rooks):
            row, _ = pos
            moves += abs(row - i)
        rooks.sort(key=lambda x: x[1])
        for i, pos in enumerate(rooks):
            _, col = pos
            moves += abs(col - i)
        return moves
