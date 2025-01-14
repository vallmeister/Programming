from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        freq = [0] * (n + 1)
        count = 0
        for i in range(n):
            ai = A[i]
            freq[ai] += 1
            if freq[ai] == 2:
                count += 1
            bi = B[i]
            freq[bi] += 1
            if freq[bi] == 2:
                count += 1
            ans.append(count)
        return ans
