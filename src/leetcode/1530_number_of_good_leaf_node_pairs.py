# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        parent = {root: None}
        leaves = set()

        def find_parents_and_leaves(node):
            if not node.left and not node.right:
                leaves.add(node)
                return
            if node.left:
                parent[node.left] = node
                find_parents_and_leaves(node.left)
            if node.right:
                parent[node.right] = node
                find_parents_and_leaves(node.right)

        find_parents_and_leaves(root)

        def dfs(node, visited, curr_dist):
            if not node or node in visited or curr_dist > distance:
                return 0
            ans = 0
            if curr_dist > 0 and node in leaves:
                ans += 1
            visited.add(node)
            ans += dfs(parent[node], visited, curr_dist + 1)
            ans += dfs(node.left, visited, curr_dist + 1)
            ans += dfs(node.right, visited, curr_dist + 1)
            return ans

        return sum(dfs(v, set(), 0) for v in leaves) // 2
