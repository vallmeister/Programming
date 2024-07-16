import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        start = None

        def find_parents(node, prev=None):
            parents[node] = prev
            if not node:
                return
            if node.left:
                find_parents(node.left, node)
            if node.right:
                find_parents(node.right, node)
            nonlocal start
            if node.val == startValue:
                start = node

        find_parents(root)

        ans = []
        curr_len = math.inf
        visited = set()
        path = []

        def backtracking(node):
            nonlocal ans, curr_len
            if node in visited:
                return
            elif node.val == destValue:
                if len(path) < curr_len:
                    curr_len = len(path)
                    ans = list(path)
                return
            visited.add(node)
            if node.left:
                path.append('L')
                backtracking(node.left)
                path.pop()
            if node.right:
                path.append('R')
                backtracking(node.right)
                path.pop()
            if parents[node]:
                path.append('U')
                backtracking(parents[node])
                path.pop()

        backtracking(start)
        return ''.join(ans)


s = Solution()
one = TreeNode(1)
two = TreeNode(2, one)
print(s.getDirections(two, 2, 1))
