# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        children = defaultdict(set)
        parent = {}
        leaves = []

        def dfs(node):
            if not node:
                return
            elif not node.left and not node.right:
                leaves.append(node)
            if node.left:
                parent[node.left] = node
                children[node].add(node.left)
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                children[node].add(node.right)
                dfs(node.right)

        dfs(root)
        ans = []
        while leaves:
            ans.append([vertex.val for vertex in leaves])
            next_leaves = []
            for leaf in leaves:
                if leaf not in parent:
                    continue
                children[parent[leaf]].remove(leaf)
                if not children[parent[leaf]]:
                    next_leaves.append(parent[leaf])
            leaves = next_leaves
        return ans
