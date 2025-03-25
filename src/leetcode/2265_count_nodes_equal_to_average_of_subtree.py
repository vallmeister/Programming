# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _, _, ans = self.helper(root)
        return ans

    def helper(self, node):
        if not node:
            return 0, 0, 0
        s1, w1, a1 = self.helper(node.left)
        s2, w2, a2 = self.helper(node.right)
        total_sum = s1 + s2 + node.val
        total_num = w1 + w2 + 1
        return total_sum, total_num, a1 + a2 + (1 if total_sum // total_num == node.val else 0)
