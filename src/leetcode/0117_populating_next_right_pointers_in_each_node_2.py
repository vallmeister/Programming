"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if root:
            q.append((root, 0))
        while q:
            node, level = q.popleft()
            if q:
                next_node, next_level = q[0]
                if level == next_level:
                    node.next = next_node
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return root