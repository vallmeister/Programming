# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heights = [[]]

        def dfs_height(node):
            if not node:
                return 0
            elif not node.left and not node.right:
                heights[0].append(node.val)
                return 0
            left_depth = dfs_height(node.left)
            right_depth = dfs_height(node.right)
            d = 1 + max(left_depth, right_depth)
            while len(heights) <= d:
                heights.append([])
            heights[d].append(node.val)
            return d

        dfs_height(root)
        return heights
