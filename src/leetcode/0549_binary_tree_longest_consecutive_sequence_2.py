# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        starting_at = defaultdict(int)
        ending_at = defaultdict(int)
        ans = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            starting_at[node] = 1
            ending_at[node] = 1
            for child in {node.left, node.right}:
                if not child:
                    continue
                elif child.val == node.val + 1:
                    starting_at[node] = max(starting_at[node], starting_at[child] + 1)
                elif child.val == node.val - 1:
                    ending_at[node] = max(ending_at[node], ending_at[child] + 1)
            nonlocal ans
            ans = max(ans, starting_at[node] + ending_at[node] - 1)

        dfs(root)
        return ans
