# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        ans = []
        while q:
            new_q = []
            curr_ans = []
            for node in q:
                if not node:
                    continue
                curr_ans.append(node.val)
                new_q.append(node.left)
                new_q.append(node.right)
            if curr_ans:
                ans.append(curr_ans)
            q = new_q
        return ans
