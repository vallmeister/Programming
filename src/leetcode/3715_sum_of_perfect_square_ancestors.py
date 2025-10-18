import math
from collections import defaultdict
from typing import List


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        g = self.get_graph(n, edges)
        kernels = self.get_kernels(nums)
        visited = [False] * n
        ancestor_kernels = defaultdict(int)

        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = True
            k = kernels[node]
            ans = ancestor_kernels[k]
            ancestor_kernels[k] += 1
            for child in g[node]:
                ans += dfs(child)
            ancestor_kernels[k] -= 1
            return ans

        return dfs(0)

    def get_graph(self, n, edges):
        adjacency_matrix = [[] for _ in range(n)]
        for u, v in edges:
            adjacency_matrix[u].append(v)
            adjacency_matrix[v].append(u)
        return adjacency_matrix

    def get_kernels(self, nums):
        kernels = []
        max_element = max(nums)
        primes = self.get_primes(int(math.sqrt(max_element)))
        for num in nums:
            for p in primes:
                square = p * p
                if square > num:
                    break
                while num % square == 0:
                    num //= square
            kernels.append(num)
        return kernels

    def get_primes(self, upper):
        primes = []
        sieve = [True] * (upper + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, upper + 1):
            if not sieve[i]:
                continue
            primes.append(i)
            for j in range(i * i, upper + 1, i):
                sieve[j] = False
        return primes


s = Solution()
print(s.sumOfAncestors(n=3, edges=[[0, 1], [1, 2]], nums=[2, 8, 2]))
print(s.sumOfAncestors(n=3, edges=[[0, 1], [0, 2]], nums=[1, 2, 4]))
print(s.sumOfAncestors(n=4, edges=[[0, 1], [0, 2], [1, 3]], nums=[1, 2, 9, 4]))
