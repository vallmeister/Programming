class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root) -> list[int]:
        if not root or root is None:
            return []
        solution = []
        solution.append(root.val)
        solution.extend(self.preorderTraversal(root.left))
        solution.extend(self.preorderTraversal(root.right))
        return solution
