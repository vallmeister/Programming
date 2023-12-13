# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_value_of_subtree = {}
        max_value_of_subtree = {}

        def get_min(node):
            if not node:
                return math.inf
            if node in min_value_of_subtree:
                return min_value_of_subtree[node]
            min_value_of_subtree[node] = min(node.val, get_min(node.left))
            return min_value_of_subtree[node]

        def get_max(node):
            if not node:
                return -math.inf
            if node in max_value_of_subtree:
                return max_value_of_subtree[node]
            max_value_of_subtree[node] = max(node.val, get_max(node.right))
            return max_value_of_subtree[node]

        def validate(node):
            if not node:
                return True
            return get_max(node.left) < node.val < get_min(node.right) and validate(node.left) and validate(node.right)

        return validate(root)


one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2, one, three)
s = Solution()
print(s.isValidBST(two))
