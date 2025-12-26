# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, 1)])
        while q:
            node, seq = q.popleft()
            if not node:
                continue
            ans = max(ans, seq)
            for child in {node.left, node.right}:
                if not child:
                    continue
                elif child.val == node.val + 1:
                    q.append((child, seq + 1))
                else:
                    q.append((child, 1))
        return ans
