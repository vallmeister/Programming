from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = []
        dummy = ListNode(next=head)
        while dummy.next:
            stack.append(dummy.next)
            dummy = dummy.next
        head = stack.pop()
        curr = head
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        return head
