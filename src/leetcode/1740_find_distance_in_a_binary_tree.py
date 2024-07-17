from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        start = None
        parent = {root: None}

        def dfs(node):
            if node.val == p:
                nonlocal start
                start = node
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)

        dfs(root)
        queue = deque()
        queue.append((start, 0))
        visited = set()
        while queue:
            node, distance = queue.popleft()
            if not node or node in visited:
                continue
            elif node.val == q:
                return distance
            visited.add(node)
            queue.append((node.left, distance + 1))
            queue.append((node.right, distance + 1))
            queue.append((parent[node], distance + 1))
        return 0
