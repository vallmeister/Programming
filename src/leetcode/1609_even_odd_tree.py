# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        even = True
        while q:
            next_q = []
            if even:
                curr = 0
            else:
                curr = 10 ** 7
            for node in q:
                if not node:
                    continue
                elif (even and not (node.val % 2 == 1 and node.val > curr)
                      or not even and not (node.val % 2 == 0 and node.val < curr)):
                    return False
                curr = node.val
                next_q.append(node.left)
                next_q.append(node.right)
            q = next_q
            even = not even
        return True
