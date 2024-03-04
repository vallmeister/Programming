from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        score = 0
        while head:
            even = head.val
            head = head.next
            odd = head.val
            head = head.next
            score += abs(even - odd) // (even - odd)
        if score > 0:
            return 'Even'
        elif score < 0:
            return 'Odd'
        else:
            return 'Tie'
