# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def dfs(self, node, curr):
        if not node:
            return
        self.values.add(curr)
        self.dfs(node.left, 2 * curr + 1)
        self.dfs(node.right, 2 * curr + 2)
