# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        leaves = []
        leaf_set = set()

        def dfs_leaves(node):
            if not node.left and not node.right and node is not root:
                leaves.append(node.val)
                leaf_set.add(node)
            else:
                if node.left:
                    dfs_leaves(node.left)
                if node.right:
                    dfs_leaves(node.right)

        dfs_leaves(root)
        left_boundary = []

        def dfs_left(node):
            if node and node not in leaf_set:
                left_boundary.append(node.val)
                if node.left:
                    dfs_left(node.left)
                elif node.right:
                    dfs_left(node.right)

        dfs_left(root.left)
        right_boundary = []

        def dfs_right(node):
            if node and node not in leaf_set:
                right_boundary.append(node.val)
                if node.right:
                    dfs_right(node.right)
                elif node.left:
                    dfs_right(node.left)

        dfs_right(root.right)
        return [root.val] + left_boundary + leaves + right_boundary[::-1]
