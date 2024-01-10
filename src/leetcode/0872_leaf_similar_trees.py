# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # TODO: use generator
        sequence_1 = []
        sequence_2 = []

        def get_sequence(node, seq):
            stack = [node]
            while stack:
                node = stack.pop()
                if not node:
                    continue
                if not node.left and not node.right:
                    seq.append(node.val)
                else:
                    stack.append(node.right)
                    stack.append(node.left)

        get_sequence(root1, sequence_1)
        get_sequence(root2, sequence_2)
        return len(sequence_1) == len(sequence_2) and all(m == n for m, n in zip(sequence_1, sequence_2))
