# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        traversal = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            traversal.append(node.val)
            inorder(node.right)
        inorder(root)

        node_to_val = {}
        suffix = 0
        for num in reversed(traversal):
            suffix += num
            node_to_val[num] = suffix

        def recursive(node):
            if not node:
                return None
            gs_node = TreeNode(node_to_val[node.val])
            gs_node.left = recursive(node.left)
            gs_node.right = recursive(node.right)
            return gs_node

        return recursive(root)
