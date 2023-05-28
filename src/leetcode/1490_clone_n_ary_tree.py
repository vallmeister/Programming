# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        def deep_copy(node):
            copy_node = Node(node.val, [])
            for child in node.children:
                copy_node.children.append(deep_copy(child))
            return copy_node

        return deep_copy(root)
