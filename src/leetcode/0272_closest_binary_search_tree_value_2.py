# Definition for a binary tree node.
from heapq import heappop, heappush
from typing import Optional, List


class TreeNode:
    # TODO: Learn Quickselect and try again
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []

        def distance(value):
            return abs(value - target)

        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)
            heappush(heap, (-distance(node.val), node.val))
            inorder_traversal(node.right)
            while len(heap) > k:
                heappop(heap)

        inorder_traversal(root)
        return [i[1] for i in heap]
