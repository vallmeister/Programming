# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def lca(node):
            if not node:
                return set()
            descendants = {node}
            descendants |= lca(node.left)
            descendants |= lca(node.right)
            nonlocal ans
            if not ans and p in descendants and q in descendants:
                ans = node
            return descendants

        lca(root)
        return ans


eight = TreeNode(8)
zero = TreeNode(0)
one = TreeNode(1)
one.left = zero
one.right = eight
four = TreeNode(4)
seven = TreeNode(7)
two = TreeNode(2)
two.left = seven
two.right = four
six = TreeNode(6)
five = TreeNode(5)
five.left = six
five.right = two
three = TreeNode(3)
three.left = five
three.right = one
s = Solution()
three = s.lowestCommonAncestor(three, five, one)


def preorder(vertex):
    if not vertex:
        return
    print(vertex.val)
    preorder(vertex.left)
    preorder(vertex.right)


preorder(three)
