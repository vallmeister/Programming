# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = self.dfs_level_sum(root, 0, [])
        root.val = 0

        def dfs(node, depth):
            if not node:
                return
            if node.left and node.right:
                c = node.left.val + node.right.val
                node.left.val = level_sum[depth + 1] - c
                node.right.val = level_sum[depth + 1] - c
            elif node.left:
                node.left.val = level_sum[depth + 1] - node.left.val
            elif node.right:
                node.right.val = level_sum[depth + 1] - node.right.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return root

    def dfs_level_sum(self, node, depth, level_sum):
        if depth >= len(level_sum):
            level_sum.append(0)
        level_sum[depth] += node.val
        if node.left:
            self.dfs_level_sum(node.left, depth + 1, level_sum)
        if node.right:
            self.dfs_level_sum(node.right, depth + 1, level_sum)
        return level_sum
