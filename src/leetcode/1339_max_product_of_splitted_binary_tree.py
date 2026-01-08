from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        subtree_sums = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            ss = node.val  # subtree sum
            ss += dfs(node.left)
            ss += dfs(node.right)
            subtree_sums[node] = ss
            return ss

        total = dfs(root)
        ans = 0
        for subtree in subtree_sums.values():
            ans = max(ans, (total - subtree) * subtree)
        return ans % MOD
