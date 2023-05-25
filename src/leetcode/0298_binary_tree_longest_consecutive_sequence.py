# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_path = 0

        def dfs(rt, curr_path):
            nonlocal max_path
            if rt is None:
                max_path = max(max_path, curr_path)
                return
            if rt.left:
                if rt.left.val == rt.val + 1:
                    dfs(rt.left, curr_path + 1)
                else:
                    dfs(rt.left, 1)
            if rt.right:
                if rt.right.val == rt.val + 1:
                    dfs(rt.right, curr_path + 1)
                else:
                    dfs(rt.right, 1)
            max_path = max(max_path, curr_path)

        dfs(root, 1)
        return max_path
