# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append((root, 0))
        ans = []
        while q:
            node, level = q.popleft()
            if not q or q[0][1] > level:
                ans.append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return ans


three = TreeNode(3)
two = TreeNode(2)
one = TreeNode(1, two)
s = Solution()
print(s.rightSideView(one))
