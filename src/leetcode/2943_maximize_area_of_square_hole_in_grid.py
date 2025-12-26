from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        side = min(self.get_longest_sequence(hBars), self.get_longest_sequence(vBars)) + 1
        return side ** 2

    def get_longest_sequence(self, arr):
        arr.sort()
        ans = curr_seq = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                curr_seq += 1
            else:
                curr_seq = 1
            ans = max(ans, curr_seq)
        return ans
