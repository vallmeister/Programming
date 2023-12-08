# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []

        def preorder_traversal(node):
            ans.append('(')
            ans.append(str(node.val))
            if node.left and node.right:
                preorder_traversal(node.left)
                preorder_traversal(node.right)
            elif node.left:
                preorder_traversal(node.left)
            elif node.right:
                ans.append('()')
                preorder_traversal(node.right)
            ans.append(')')

        if root:
            preorder_traversal(root)

        n = len(ans)
        return ''.join(ans[1:n - 1])

    # TODO: Make stack solution
    def tree_2_str(self, root):
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(str(node.val))
            if not node.left and not node.right:
                continue
            ans.append('(')
            if node.right:
                stack.append(node.right)
            stack.append(node.left)

        return ''.join(ans)


s = Solution()
four = TreeNode(4)
two = TreeNode(2, left=four)
three = TreeNode(3)
one = TreeNode(1, two, three)
print(s.tree2str(one))
print(s.tree_2_str(one))
