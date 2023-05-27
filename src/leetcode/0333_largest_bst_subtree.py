# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_size = 1

        def traverse(node):
            nonlocal max_size
            if node is None:
                return 0, math.inf, -math.inf, True
            l_size, l_min, l_max, l_bst = traverse(node.left)
            r_size, r_min, r_max, r_bst = traverse(node.right)
            is_bst = l_bst and r_bst and l_max < node.val < r_min
            size = l_size + r_size + 1
            if is_bst:
                max_size = max(max_size, size)
            return size, min(l_min, node.val), max(r_max, node.val), is_bst

        traverse(root)
        return max_size


s = Solution()
