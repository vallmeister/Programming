from collections import deque
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        q = deque()
        [q.append(i) for i in arr]
        last_winner = q.popleft()
        win_count = 0
        while True:
            challenger = q.popleft()
            if last_winner > challenger:
                q.append(challenger)
                win_count += 1
            elif last_winner < challenger:
                q.append(last_winner)
                last_winner = challenger
                win_count = 1
            if win_count == k:
                return last_winner


s = Solution()
print(s.getWinner([2, 1, 3, 5, 4, 6, 7], k=2))
print(s.getWinner([3, 2, 1], k=10))
print(s.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
