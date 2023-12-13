# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sum = []
        level_num_nodes = []
        q = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if not node:
                continue
            if level >= len(level_sum):
                level_sum.append(node.val)
                level_num_nodes.append(1)
            else:
                level_sum[level] += node.val
                level_num_nodes[level] += 1
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        return [round(level_sum[i] / level_num_nodes[i], 5) for i in range(len(level_sum))]
