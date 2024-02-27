from collections import defaultdict, deque
from math import sqrt
from typing import List


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        prime_adjacency = defaultdict(set)
        node_adjacency = defaultdict(set)

        for i in range(n):
            x = nums[i]
            while x % 2 == 0:
                prime_adjacency[2].add(i)
                node_adjacency[i].add(2)
                x /= 2
            for j in range(3, int(sqrt(x) + 1), 2):
                while x % j == 0:
                    prime_adjacency[j].add(i)
                    node_adjacency[i].add(j)
                    x /= j
            if x > 2:
                prime_adjacency[x].add(i)
                node_adjacency[i].add(x)

        q = deque()
        visited_nodes = set()
        visited_primes = set()
        q.append((0, True))
        while q:
            index, is_node = q.popleft()
            if is_node:
                if index in visited_nodes:
                    continue
                visited_nodes.add(index)
                for prime in node_adjacency[index]:
                    q.append((prime, False))
            else:
                if index in visited_primes:
                    continue
                visited_primes.add(index)
                for node in prime_adjacency[index]:
                    q.append((node, True))
        return all(i in visited_nodes for i in range(n))
