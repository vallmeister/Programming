from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] ^ arr[i - 1]

        ans = []
        for left, right in queries:
            ans.append(ps[right + 1] ^ ps[left])
        return ans
