from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode()]
        ans = []
        for i in range(1, n - 1, 2):
            l = self.allPossibleFBT(i)
            r = self.allPossibleFBT(n - i - 1)
            for lc in l:
                for rc in r:
                    ans.append(TreeNode(left=lc, right=rc))
        return ans
