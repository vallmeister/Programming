class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root) -> list[int]:
        if root is None:
            return []
        traversal = []
        traversal.extend(self.postorderTraversal(root.left))
        traversal.extend(self.postorderTraversal(root.right))
        traversal.append(root.val)
        return traversal
    