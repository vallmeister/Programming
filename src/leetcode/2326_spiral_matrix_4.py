# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cd = 0
        row = col = 0
        left = top = -1
        while head:
            mat[row][col] = head.val
            dr, dc = dirs[cd]
            if cd == 0 and col + dc == n:
                cd = 1
                row += 1
                top += 1
            elif cd == 1 and row + dr == m:
                cd = 2
                col -= 1
                n -= 1
            elif cd == 2 and col + dc == left:
                cd = 3
                row -= 1
                m -= 1
            elif cd == 3 and row + dr == top:
                cd = 0
                col += 1
                left += 1
            else:
                row += dr
                col += dc
            head = head.next
        return mat
    