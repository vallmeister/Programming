# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val < low:
                stack.append(node.right)
            elif low <= node.val <= high:
                ans += node.val
                stack.append(node.right)
                stack.append(node.left)
            elif high < node.val:
                stack.append(node.left)
        return ans
