from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, prev):
            prev += node.val
            if not node.left and not node.right:
                return prev
            ans = 0
            if node.left:
                ans += dfs(node.left, 2 * prev)
            if node.right:
                ans += dfs(node.right, 2 * prev)
            return ans

        return dfs(root, 0)
