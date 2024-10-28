# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights_after_rm = {}
        heights = {}

        def dfs_height(node):
            if not node:
                return -1
            if node.val in heights:
                return heights[node.val]
            heights[node.val] = 1 + max(dfs_height(node.left), dfs_height(node.right))
            return heights[node.val]

        dfs_height(root)

        def dfs(node, depth, max_val):
            if not node:
                return
            heights_after_rm[node.val] = max_val
            dfs(node.left, depth + 1, max(max_val, depth + 1 + dfs_height(node.right)))
            dfs(node.right, depth + 1, max(max_val, depth + 1 + dfs_height(node.left)))

        dfs(root, 0, 0)
        return [heights_after_rm[i] for i in queries]


s = Solution()
two = TreeNode(val=2)
three = TreeNode(val=3, left=two)
seven = TreeNode(val=7)
six = TreeNode(val=6)
five = TreeNode(val=5, right=seven)
four = TreeNode(val=4, left=six, right=five)
one = TreeNode(val=1, left=three, right=four)
print(s.treeQueries(one, [4]))
