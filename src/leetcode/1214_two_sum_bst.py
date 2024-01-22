from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def inorder(node, nums):
            if not node:
                return
            inorder(node.left, nums)
            nums.append(node.val)
            inorder(node.right, nums)

        nums_1 = []
        nums_2 = []
        inorder(root1, nums_1)
        inorder(root2, nums_2)

        i = 0
        j = len(nums_2) - 1
        while i < len(nums_1) and j >= 0:
            s = nums_1[i] + nums_2[j]
            if s == target:
                return True
            elif s < target:
                i += 1
            elif s > target:
                j -= 1
        return False
