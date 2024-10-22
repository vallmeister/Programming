# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        curr_nodes = [root]
        while curr_nodes:
            children = []
            curr_sum = 0
            for node in curr_nodes:
                curr_sum += node.val
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            sums.append(curr_sum)
            curr_nodes = children
        sums.sort(reverse=True)
        return sums[k - 1] if len(sums) >= k else -1
