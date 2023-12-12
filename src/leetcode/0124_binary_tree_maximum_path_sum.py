# Definition for a binary tree node.
import math
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sub_path = defaultdict(int)
        ans = -math.inf

        def recursive(node):
            if not node:
                return 0
            left_path = recursive(node.left)
            right_path = recursive(node.right)
            max_sub_path[node] = max(left_path, right_path, 0)
            nonlocal ans
            ans = max(ans, max(left_path, 0) + max(right_path, 0) + node.val)
            return max_sub_path[node] + node.val

        recursive(root)
        return int(ans)
