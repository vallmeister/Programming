from heapq import heappop, heappush
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        heap = []

        def find_leaves(node, level):
            if not node.left and not node.right:
                heappush(heap, (level, node.val))
            else:
                if node.left:
                    find_leaves(node.left, level - 1)
                if node.right:
                    find_leaves(node.right, level - 1)

        find_leaves(root, 0)
        level, leave_sum = heappop(heap)
        while heap:
            l, ls = heappop(heap)
            if l > level:
                break
            leave_sum += ls
        return leave_sum
