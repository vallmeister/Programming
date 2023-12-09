# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def recursive(node):
            if not node:
                return
            recursive(node.left)
            ans.append(node.val)
            recursive(node.right)

        recursive(root)
        return ans

    def inorder_traversal_stack(self, root):
        ans = []
        visited = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node in visited:
                ans.append(node.val)
                continue
            visited.add(node)
            stack.append(node.right)
            stack.append(node)
            stack.append(node.left)
        return ans
