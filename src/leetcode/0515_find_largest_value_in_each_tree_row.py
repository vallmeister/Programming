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
        q = []
        if root:
            q.append(root)
        while q:
            next_q = []
            curr_max = -math.inf
            for node in q:
                curr_max = max(curr_max, node.val)
                left, right = node.left, node.right
                if left:
                    next_q.append(left)
                if right:
                    next_q.append(right)
            ans.append(curr_max)
            q = next_q
        return ans


s = Solution()
# print(s.largestValues([1, 3, 2, 5, 3, None, 9]))
# print(s.largestValues([1, 2, 3]))
