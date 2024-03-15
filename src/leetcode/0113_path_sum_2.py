# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node, path, s):
            v = node.val
            path.append(v)
            s += v
            if not node.left and not node.right:
                if s == targetSum:
                    ans.append(list(path))
            if node.left:
                dfs(node.left, path, s)
            if node.right:
                dfs(node.right, path, s)
            path.pop()
            s -= v

        if root:
            dfs(root, [], 0)
        return ans
