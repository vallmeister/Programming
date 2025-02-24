# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.index = 0

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self.helper(traversal, 0)

    def helper(self, traversal, depth):
        if self.index >= len(traversal):
            return None

        dash_count = 0
        while self.index + dash_count < len(traversal) and traversal[self.index + dash_count] == '-':
            dash_count += 1

        if dash_count != depth:
            return None

        self.index += dash_count

        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = 10 * value + int(traversal[self.index])
            self.index += 1

        node = TreeNode(value)
        node.left = self.helper(traversal, depth + 1)
        node.right = self.helper(traversal, depth + 1)
        return node
