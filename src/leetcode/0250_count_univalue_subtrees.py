# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def is_uni_value(node):
            nonlocal count
            if node is None:
                return True
            elif node.left and node.right:
                lft = is_uni_value(node.left)
                rgt = is_uni_value(node.right)
                if lft and rgt and node.left.val == node.val == node.right.val:
                    count += 1
                    return True
                else:
                    return False
            elif node.left:
                if is_uni_value(node.left) and node.val == node.left.val:
                    count += 1
                    return True
                else:
                    return False
            elif node.right:
                if is_uni_value(node.right) and node.val == node.right.val:
                    count += 1
                    return True
                else:
                    return False
            else:
                count += 1
                return True

        is_uni_value(root)
        return count
