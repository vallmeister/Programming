# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def find_root(node):
            if not node.parent:
                return node
            return find_root(node.parent)

        root = find_root(p)
        ans = None

        def find_descendants(node):
            nonlocal ans
            if not node or ans:
                return set()
            descendants = find_descendants(node.left) | find_descendants(node.right) | {node}
            if not ans and p in descendants and q in descendants:
                ans = node
            return descendants

        find_descendants(root)
        return ans
