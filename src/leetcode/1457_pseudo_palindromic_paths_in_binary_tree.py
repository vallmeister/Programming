# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0
        visited = [0] * 10

        def backtracking(node, curr_len):
            visited[node.val] += 1
            curr_len += 1
            if not node.left and not node.right:
                nonlocal ans
                if curr_len % 2 == 0 and all(count % 2 == 0 for count in visited):
                    ans += 1
                elif curr_len % 2 == 1 and sum(1 if count % 2 == 1 else 0 for count in visited) <= 1:
                    ans += 1
            else:
                if node.left:
                    backtracking(node.left, curr_len)
                if node.right:
                    backtracking(node.right, curr_len)
            visited[node.val] -= 1
            curr_len -= 1
            return

        backtracking(root, 0)
        return ans

    def pseudo_palindromic_paths(self, root):
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            path ^= (1 << node.val)
            if not node.left and not node.right and path & (path - 1) == 0:
                ans += 1
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))
        return ans


six = TreeNode(1)
five = TreeNode(1)
four = TreeNode(3)
three = TreeNode(1, right=six)
two = TreeNode(3, four, five)
root = TreeNode(2, two, three)
s = Solution()
print(s.pseudoPalindromicPaths(root))
