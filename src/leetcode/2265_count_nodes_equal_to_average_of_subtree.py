# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            l_size = r_size = 0
            l_sum = r_sum = 0
            nonlocal ans
            if node.left:
                l_size, l_sum = dfs(node.left)
            if node.right:
                r_size, r_sum = dfs(node.right)
            total_size = l_size + r_size + 1
            total_sum = l_sum + r_sum + node.val
            if total_sum // total_size == node.val:
                ans += 1
            return total_size, total_sum

        dfs(root)
        return ans
    