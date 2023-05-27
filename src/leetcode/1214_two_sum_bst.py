from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        t1_values = set()
        t2_values = set()

        def traverse(node, mem):
            if node is None:
                return
            mem.add(node.val)
            traverse(node.left, mem)
            traverse(node.right, mem)

        if root1.val + root2.val < target:
            root1.left = None
            root2.left = None
        elif root1.val + root2.val > target:
            root1.right = None
            root2.right = None
        else:
            return True
        traverse(root1, t1_values)
        traverse(root2, t2_values)
        for val in t1_values:
            if target - val in t2_values:
                return True
        return False
