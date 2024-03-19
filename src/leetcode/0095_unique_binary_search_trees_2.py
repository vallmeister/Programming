# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def recursive(start, end):
            if start > end:
                return [None]
            ans = []
            for i in range(start, end + 1):
                for lf in recursive(start, i - 1):
                    for rt in recursive(i + 1, end):
                        root = TreeNode(i)
                        root.left = lf
                        root.right = rt
                        ans.append(root)
            return ans

        return recursive(1, n)


s = Solution()
print(s.generateTrees(3))
