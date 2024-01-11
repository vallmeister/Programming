# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def recursive(node, min_ancestor, max_ancestor):
            diff = max(abs(min_ancestor - node.val), abs(max_ancestor - node.val))
            min_ancestor = min(min_ancestor, node.val)
            max_ancestor = max(max_ancestor, node.val)
            diff_left = 0
            diff_right = 0
            if node.left:
                diff_left = recursive(node.left, min_ancestor, max_ancestor)
            if node.right:
                diff_right = recursive(node.right, min_ancestor, max_ancestor)
            return max(diff, diff_left, diff_right)

        return recursive(root, root.val, root.val)
