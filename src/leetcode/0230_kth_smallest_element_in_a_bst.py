from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from src.leetcode.MaximumDepthBinaryTree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pointer = 0
        element = None

        def inorder(node):
            nonlocal element
            if not node or element:
                return
            inorder(node.left)
            nonlocal pointer
            pointer += 1
            if pointer == k:
                element = node.val
                return
            inorder(node.right)

        inorder(root)
        return element
