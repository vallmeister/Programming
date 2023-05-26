# Definition for a binary tree node.
from heapq import heappop, heappush
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        closest_heap = []

        def dfs(node):
            if node is None:
                return
            distance = -abs(node.val - target)
            heappush(closest_heap, (distance, node.val))
            while len(closest_heap) > k:
                heappop(closest_heap)
            if target <= node.val:
                dfs(node.left)
                if len(closest_heap) < k:
                    dfs(node.right)
            else:
                dfs(node.right)
                if len(closest_heap) < k:
                    dfs(node.left)

        dfs(root)
        return [i[1] for i in closest_heap]
