# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sentinel = ListNode(next=head)
        slow = fast = sentinel
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(ls):
            prev = None
            while ls:
                next_tmp = ls.next
                ls.next = prev
                prev = ls
                ls = next_tmp
            return prev

        tail = slow.next
        slow.next = None
        tail = reverse(tail)
        while head and tail:
            next_head = head.next
            head.next = tail
            next_tail = tail.next
            head = next_head
            tail.next = head
            tail = next_tail
