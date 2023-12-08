# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = -math.inf

        def recursive(node):
            if not node:
                return 0, 0
            num_nodes = 1
            val = node.val
            num_nodes_sub, val_sub = recursive(node.left)
            num_nodes += num_nodes_sub
            val += val_sub
            num_nodes_sub, val_sub = recursive(node.right)
            num_nodes += num_nodes_sub
            val += val_sub
            nonlocal ans
            ans = max(ans, val / num_nodes)
            return num_nodes, val

        recursive(root)
        return ans


s = Solution()
two = TreeNode(2)
one = TreeNode(1)
three = TreeNode(3, two, one)
zero = TreeNode(0, three)
print(s.maximumAverageSubtree(zero))

six = TreeNode(6)
five = TreeNode(5, six, one)
print(s.maximumAverageSubtree(five))
