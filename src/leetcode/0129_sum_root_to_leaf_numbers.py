# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, curr = stack.pop()
            curr *= 10
            curr += node.val
            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))
            if not node.left and not node.right:
                ans += curr
        return ans
