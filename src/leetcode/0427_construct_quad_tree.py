from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:

        def recursive(n, row, col):
            if n == 1:
                return Node(bool(grid[row][col]), True, None, None, None, None)
            mid = n // 2
            top_left = recursive(mid, row, col)
            top_right = recursive(mid, row, col + mid)
            bottom_left = recursive(mid, row + mid, col)
            bottom_right = recursive(mid, row + mid, col + mid)
            if top_left.val and top_right.val and bottom_left.val and bottom_right.val:
                return Node(True, True, None, None, None, None)
            # TODO: Rethink how to prune tree
            elif not top_left.val and not top_right.val and not bottom_left.val and not bottom_right.val:
                return Node(False, True, None, None, None, None)
            else:
                return Node(False, False, top_left, top_right, bottom_left, bottom_right)

        return recursive(len(grid), 0, 0)


s = Solution()
print(s.construct([[0, 1], [1, 0]]))
print(s.construct(
    [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]))
