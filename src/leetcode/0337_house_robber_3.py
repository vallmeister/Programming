# Definition for a binary tree node.
from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def memo(node, skip):
            if not node:
                return 0
            elif skip:
                return memo(node.left, False) + memo(node.right, False)
            else:
                return max(memo(node.left, False) + memo(node.right, False),
                           node.val + memo(node.left, True) + memo(node.right, True))

        return memo(root, False)
