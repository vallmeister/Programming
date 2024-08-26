# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        traversal = []
        if not root:
            return traversal
        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                traversal.append(node.val)
            else:
                visited.add(node)
                stack.append(node)
                for child in reversed(node.children):
                    stack.append(child)
        return traversal
