# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        q = [root]
        while q:
            curr = []
            next_q = []
            for node in q:
                if not node:
                    continue
                curr.append(node.val)
                if node.left:
                    next_q.extend([node.left, node.right])
            q = next_q
            values.append(curr)

        ans = TreeNode(values[0][0])
        q = [ans]
        for level, curr_values in enumerate(values):
            next_q = []
            if level % 2 == 1:
                curr_values.reverse()
            for i, node in enumerate(q):
                node.val = curr_values[i]
                if level < len(values) - 1:
                    left, right = TreeNode(), TreeNode()
                    node.left, node.right = left, right
                    next_q.extend([left, right])
            q = next_q

        return ans


def get_tree_node(nums):
    root = TreeNode(val=nums[0])
    q = [(root, 0)]
    while q:
        next_q = []
        for node, index in q:
            if 2 * index + 1 >= len(nums):
                continue
            node.left = TreeNode(val=nums[2 * index + 1])
            node.right = TreeNode(val=nums[2 * index + 2])
            next_q.append((node.left, 2 * index + 1))
            next_q.append((node.right, 2 * index + 2))
        q = next_q
    return root


s = Solution()
tree = get_tree_node([2, 3, 5, 8, 13, 21, 34])
print(s.reverseOddLevels(tree))
