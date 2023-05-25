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
        max_avg = -math.inf

        def dfs(node):
            nonlocal max_avg
            if node is None:
                return 0.0, 0.0
            left_sum, left_size = dfs(node.left)
            right_sum, right_size = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_size = left_size + right_size + 1
            max_avg = max(max_avg, total_sum / total_size)
            return total_sum, total_size

        dfs(root)
        return max_avg


s = Solution()
two = TreeNode(2)
one = TreeNode(1)
three = TreeNode(3, two, one)
root = TreeNode(0, three)
print(s.maximumAverageSubtree(root))
