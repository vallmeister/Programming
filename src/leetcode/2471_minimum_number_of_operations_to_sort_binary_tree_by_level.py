from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [root]
        while q:
            next_q = []
            values = []
            for node in q:
                if not node:
                    continue
                values.append(node.val)
                next_q.append(node.left)
                next_q.append(node.right)
            res += self.get_operations(values)
            q = next_q
        return res

    def get_operations(self, arr):
        ops = 0
        target = list(sorted(arr))
        indices = {num: i for i, num in enumerate(arr)}
        for i in range(len(arr)):
            if arr[i] != target[i]:
                ops += 1
                j = indices[target[i]]
                arr[i], arr[j] = arr[j], arr[i]
                indices[arr[i]] = i
                indices[arr[j]] = j
        return ops
