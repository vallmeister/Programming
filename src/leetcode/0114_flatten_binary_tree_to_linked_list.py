# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        stack = []
        while curr:
            if curr.left and curr.right:
                stack.append(curr.right)
                curr.left, curr.right = None, curr.left
            elif curr.left:
                curr.left, curr.right = None, curr.left
            elif not curr.right and stack:
                curr.right = stack.pop()
            curr = curr.right


s = Solution()
five = TreeNode(5)
four = TreeNode(4)
three = TreeNode(3, left=five)
two = TreeNode(2, left=three, right=four)
one = TreeNode(1, left=two)
s.flatten(one)
while one:
    print(one.val)
    one = one.right
