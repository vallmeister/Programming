import math
from collections import defaultdict
from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        ans = [0] * n
        subtree_sizes = [0] * n
        top_coins = defaultdict(list)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)

        def subtree_sizes_and_coins(node):
            size = 1
            tree_coins = [cost[node]]
            for neighbor in tree[node]:
                sub_size, sub_coins = subtree_sizes_and_coins(neighbor)
                size += sub_size
                tree_coins.extend(sub_coins)
            subtree_sizes[node] = size
            tree_coins.sort(reverse=True)
            top_coins[node] = tree_coins[:3] + tree_coins[-2:]
            top_coins[node].sort(reverse=True)
            return size, tree_coins

        subtree_sizes_and_coins(0)
        for v in range(n):
            if subtree_sizes[v] < 3:
                ans[v] = 1
                continue
            coins = top_coins[v]
            ans[v] = max(0, math.prod(coins[:3]), coins[0] * math.prod(coins[-2:]))
        return ans


s = Solution()
print(s.placedCoins([[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], cost=[1, 2, 3, 4, 5, 6]))
print(
    s.placedCoins([[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]], cost=[1, 4, 2, 3, 5, 7, 8, -4, 2]))
print(s.placedCoins([[0, 1], [0, 2]], cost=[1, 2, -2]))
