from collections import deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1

        root = find_root()
        if root == -1:
            return False
        visited = set()
        q = deque()
        q.append(root)
        while q:
            v = q.popleft()
            if v in visited:
                return False
            visited.add(v)
            left, right = leftChild[v], rightChild[v]
            if left != -1:
                q.append(left)
            if right != -1:
                q.append(right)
        return len(visited) == n


s = Solution()
print(s.validateBinaryTreeNodes(4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(s.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(s.validateBinaryTreeNodes(2, leftChild=[1, 0], rightChild=[-1, -1]))
print(s.validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]))
print(s.validateBinaryTreeNodes(5, [1, 3, -1, -1, -1], [-1, 2, 4, -1, -1]))
