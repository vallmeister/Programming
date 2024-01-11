# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacency_matrix_to = defaultdict(list)
        start_node = None

        def dfs(node):
            if node.val == start:
                nonlocal start_node
                start_node = node
            if node.left:
                adjacency_matrix_to[node].append(node.left)
                dfs(node.left)
            if node.right:
                adjacency_matrix_to[node].append(node.right)
                dfs(node.right)

        dfs(root)
        adjacency_matrix_from = defaultdict(list)
        for v, neighborhood in adjacency_matrix_to.items():
            for u in neighborhood:
                adjacency_matrix_from[u].append(v)
        visited = set()
        ans = 0
        q = deque()
        q.append((start_node, 0))
        while q:
            vertex, time = q.popleft()
            if vertex.val in visited:
                continue
            visited.add(vertex.val)
            ans = max(ans, time)
            adjacency_matrix_to[vertex].extend(adjacency_matrix_from[vertex])
            for neighbor in adjacency_matrix_to[vertex]:
                q.append((neighbor, time + 1))
        return ans
