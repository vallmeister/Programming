# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                continue
            modes[node.val] += 1
            q.append(node.left)
            q.append(node.right)
        max_cnt = max(modes.values())
        return [element for element, count in modes.items() if count == max_cnt]
