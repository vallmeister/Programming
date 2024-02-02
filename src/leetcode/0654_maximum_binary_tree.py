# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(i, j):
            if j < i:
                return None
            elif i == j:
                return TreeNode(nums[i])
            max_so_far = -1
            idx = -1
            for k in range(i, j + 1):
                if nums[k] > max_so_far:
                    idx = k
                    max_so_far = nums[k]
            left = construct(i, idx - 1)
            right = construct(idx + 1, j)
            return TreeNode(max_so_far, left, right)

        return construct(0, len(nums) - 1)
