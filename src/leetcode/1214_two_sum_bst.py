from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def search(node, num):
            if not node:
                return False
            elif node.val == num:
                return True
            elif num < node.val:
                return search(node.left, num)
            else:
                return search(node.right, num)

        def dfs(node):
            if not node:
                return False
            return search(root2, target - node.val) or dfs(node.left) or dfs(node.right)

        return dfs(root1)
