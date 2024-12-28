# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}

        def dfs(node):
            if node.left:
                parents[node.left] = node
                dfs(node.left)
            if node.right:
                parents[node.right] = node
                dfs(node.right)

        dfs(root)
        if p not in parents or q not in parents:
            return None

        def get_path(node):
            path = []
            while node:
                path.append(node)
                node = parents[node]
            return path

        p_path = get_path(p)
        p_path.reverse()

        q_path = get_path(q)
        q_path.reverse()

        ans = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                ans = p_path[i]
        return ans
