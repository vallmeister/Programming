# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {inorder[i]: i for i in range(len(inorder))}

        def recursive(i, j):
            if i > j:
                return None
            nonlocal preorder_index
            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_value)
            root.left = recursive(i, inorder_index_map[root_value] - 1)
            root.right = recursive(inorder_index_map[root_value] + 1, j)
            return root

        preorder_index = 0
        return recursive(0, len(preorder) - 1)
