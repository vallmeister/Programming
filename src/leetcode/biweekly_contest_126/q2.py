from heapq import heapify, heappop
from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(nums)
        heap = [(v, k) for k, v in enumerate(nums)]
        heapify(heap)
        marked = set()
        ans = []
        for index, k in queries:
            num = nums[index]
            if (num, index) not in marked:
                s -= num
            marked.add((num, index))
            while heap and k > 0:
                value, key = heappop(heap)
                if (value, key) in marked:
                    continue
                marked.add((value, key))
                s -= value
                k -= 1
            ans.append(s)
        return ans


sol = Solution()
print(sol.unmarkedSumArray([1, 2, 2, 1, 2, 3, 1], queries=[[1, 2], [3, 3], [4, 2]]))
print(sol.unmarkedSumArray([1, 4, 2, 3], queries=[[0, 1]]))
