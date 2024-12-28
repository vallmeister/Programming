import math
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = [root]
        while q:
            mx = -math.inf
            nq = []
            for node in q:
                if not node:
                    continue
                mx = max(mx, node.val)
                nq.extend([node.left, node.right])
            q = nq
            if mx > -math.inf:
                ans.append(mx)
        return ans


s = Solution()
two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1, two, three)
print(s.largestValues(one))
