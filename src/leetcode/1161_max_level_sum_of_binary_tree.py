import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_sum = -math.inf
        q = [root]
        level = 0
        while q:
            next_q = []
            level += 1
            curr_sum = 0
            for node in q:
                curr_sum += node.val
                for child in {node.left, node.right}:
                    if child:
                        next_q.append(child)
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level
            q = next_q
        return ans
