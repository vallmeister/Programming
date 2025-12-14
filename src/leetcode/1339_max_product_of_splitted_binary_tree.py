from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sum = defaultdict(int)

        def dfs_sum(node):
            if not node:
                return 0
            ans = node.val + dfs_sum(node.left) + dfs_sum(node.right)
            subtree_sum[node] = ans
            return ans

        MOD = 10 ** 9 + 7
        total = dfs_sum(root)

        def dfs_split(node):
            if not node:
                return 0
            curr = subtree_sum[node]
            subtree_prod = curr * (total - curr)
            subtree_prod %= MOD
            return max(subtree_prod, dfs_split(node.left), dfs_split(node.right))

        return dfs_split(root)
