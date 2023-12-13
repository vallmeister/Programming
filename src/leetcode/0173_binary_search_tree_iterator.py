from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.ptr = -1

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            self.inorder.append(node.val)
            traverse(node.right)
        traverse(root)

    def next(self) -> int:
        self.ptr += 1
        return self.inorder[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr < len(self.inorder) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
