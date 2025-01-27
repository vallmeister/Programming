from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        root = list(range(n))
        rank = [1] * n

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rank[rx] > rank[ry]:
                    root[ry] = rx
                elif rank[rx] < rank[ry]:
                    root[rx] = ry
                else:
                    root[ry] = rx
                    rank[rx] += 1

        sorted_nums = list(sorted((num, idx) for idx, num in enumerate(nums)))
        prev_num, prev_idx = sorted_nums[0]
        for num, idx in sorted_nums[1:]:
            if abs(num - prev_num) <= limit:
                union(idx, prev_idx)
            prev_num, prev_idx = num, idx

        components = defaultdict(list)
        for i in range(n):
            ri = find(i)
            heappush(components[ri], nums[i])

        ans = []
        for i in range(n):
            ri = find(i)
            comp = components[ri]
            ans.append(heappop(comp))
        return ans


s = Solution()
print(s.lexicographicallySmallestArray([1, 5, 3, 9, 8], 2))
print(s.lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], 3))
print(s.lexicographicallySmallestArray([1, 7, 28, 19, 10], 3))
