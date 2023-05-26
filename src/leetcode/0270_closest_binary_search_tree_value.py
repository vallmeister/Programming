# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_so_far = root.val

        def dfs(node):
            if node is None:
                return
            nonlocal closest_so_far
            if abs(node.val - target) < abs(closest_so_far - target):
                closest_so_far = node.val
            elif abs(node.val - target) == abs(closest_so_far - target):
                closest_so_far = min(closest_so_far, node.val)
            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)

        dfs(root)
        return closest_so_far
