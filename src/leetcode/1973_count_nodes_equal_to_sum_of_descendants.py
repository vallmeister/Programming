# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def d_sum(node):
            if not node:
                return 0
            s = d_sum(node.left) + d_sum(node.right)
            if s == node.val:
                nonlocal ans
                ans += 1
            return s + node.val

        d_sum(root)
        return ans
