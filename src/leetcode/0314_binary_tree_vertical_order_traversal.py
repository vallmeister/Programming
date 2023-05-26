# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        traversal = defaultdict(list)
        min_width = 0
        max_width = 0
        q = deque()
        q.append((root, 0))
        while q:
            node, vertical = q.popleft()
            min_width = min(min_width, vertical)
            max_width = max(max_width, vertical)
            traversal[vertical].append(node.val)
            if node.left:
                q.append((node.left, vertical - 1))
            if node.right:
                q.append((node.right, vertical + 1))

        ans = []
        for i in range(min_width, max_width + 1):
            ans.append(traversal[i])
        return ans
