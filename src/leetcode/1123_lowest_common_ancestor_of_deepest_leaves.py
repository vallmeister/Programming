from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depths = []
        parent = {root: None}

        def dfs(node, level):
            if level == len(depths):
                depths.append([])
            depths[level].append(node)
            if node.left:
                parent[node.left] = node
                dfs(node.left, level + 1)
            if node.right:
                parent[node.right] = node
                dfs(node.right, level + 1)

        dfs(root, 0)
        deepest_leaves = depths[-1]
        paths = []
        for leaf in deepest_leaves:
            path = []
            while leaf:
                path.append(leaf)
                leaf = parent[leaf]
            path.reverse()
            paths.append(path)
        n = min(len(path) for path in paths)
        for i in range(n):
            if any(paths[0][i] != path[i] for path in paths):
                return paths[0][i - 1]
        return paths[0][n - 1]
