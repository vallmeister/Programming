# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        prev = ListNode(next=head)
        curr = head
        new_head = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                if curr is new_head:
                    new_head = new_head.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return new_head


s = Solution()
fourth = ListNode(1)
third = ListNode(2, fourth)
second = ListNode(2, third)
first = ListNode(1, second)
head = s.removeElements(first, 2)
while head:
    print(head.val)
    head = head.next
