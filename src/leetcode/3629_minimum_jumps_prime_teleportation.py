from collections import defaultdict
from typing import List


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        factors = self.get_factors(max(nums))
        edges = defaultdict(list)
        for i, num in enumerate(nums):
            for p in factors[num]:
                edges[p].append(i)

        q = [0]
        ans = 0
        visited = [False] * n
        while q:
            next_q = []
            for i in q:
                if i == n - 1:
                    return ans
                visited[i] = True
                if i > 0 and not visited[i - 1]:
                    next_q.append(i - 1)
                if i < n - 1 and not visited[i + 1]:
                    next_q.append(i + 1)
                num = nums[i]
                if len(factors[num]) != 1:
                    continue
                for j in edges[num]:
                    if i == j or visited[j]:
                        continue
                    next_q.append(j)
                edges[num].clear()
            ans += 1
            q = next_q
        return n

    def get_factors(self, n):
        factors = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            if factors[i]:
                continue
            for j in range(i, n + 1, i):
                factors[j].append(i)
        return factors


s = Solution()
print(s.minJumps(nums=[1, 2, 4, 6]))
print(s.minJumps(nums=[2, 3, 4, 7, 9]))
print(s.minJumps(nums=[4, 6, 5, 8]))
print(s.minJumps([13, 169, 43, 275, 244, 143, 195, 28, 165, 186, 103, 185, 166, 172, 172, 244, 250, 257]))  # 6
