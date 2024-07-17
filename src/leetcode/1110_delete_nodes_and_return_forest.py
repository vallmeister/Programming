from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        parent = {root: (None, False)}

        def find_parents(node):
            if node.left:
                parent[node.left] = (node, False)
                find_parents(node.left)
            if node.right:
                parent[node.right] = (node, True)
                find_parents(node.right)

        find_parents(root)

        def dfs(node, to_append=True):
            if not node:
                return

            if node.val in to_delete:
                p_node, is_right = parent[node]
                if p_node and is_right:
                    p_node.right = None
                elif p_node:
                    p_node.left = None
                to_append = True
            elif to_append:
                forest.append(node)
                to_append = False

            dfs(node.left, to_append)
            dfs(node.right, to_append)

        dfs(root)
        return forest
