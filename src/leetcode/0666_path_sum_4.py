from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        nodes_by_depth_and_pos = {}
        for num in nums:
            v = num % 10
            num //= 10
            p = num % 10 - 1
            num //= 10
            d = num % 10
            node = TreeNode(v)
            nodes_by_depth_and_pos[(d, p)] = node
            if d > 1:
                if p % 2 == 0:  # left child
                    nodes_by_depth_and_pos[(d - 1, p // 2)].left = node
                else:  # right child
                    nodes_by_depth_and_pos[(d - 1, p // 2)].right = node
        root = nodes_by_depth_and_pos[(1, 0)]
        return self.dfs(root, 0)

    def dfs(self, node, curr_sum):
        curr_sum += node.val
        if not node.left and not node.right:
            return curr_sum
        s = 0
        if node.left:
            s += self.dfs(node.left, curr_sum)
        if node.right:
            s += self.dfs(node.right, curr_sum)
        return s


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


sol = Solution()
print(sol.pathSum([113, 215, 221]))
print(sol.pathSum([113, 221]))
