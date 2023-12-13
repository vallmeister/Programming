# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = [root]
        while q:
            next_q = []
            curr_level = []
            for node in q:
                if not node:
                    continue
                curr_level.append(node.val)
                next_q.append(node.left)
                next_q.append(node.right)
            if curr_level:
                ans.append(curr_level)
            q = next_q
        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]
        return ans


four = TreeNode(4)
five = TreeNode(5)
two = TreeNode(2, left=four)
three = TreeNode(3, right=five)
one = TreeNode(1, left=two, right=three)
print(Solution().zigzagLevelOrder(one))
