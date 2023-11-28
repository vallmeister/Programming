# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev_1 = dummy
        curr_1 = dummy.next
        while curr_1:
            prev_2 = curr_1
            curr_2 = curr_1.next
            while curr_2:
                if curr_1.val > curr_2.val:
                    prev_1.next, prev_2.next = curr_2, curr_1
                    curr_1.next, curr_2.next = curr_2.next, curr_1.next
                    curr_1, curr_2 = curr_2, curr_1
                prev_2, curr_2 = curr_2, curr_2.next
            prev_1, curr_1 = curr_1, curr_1.next
        return dummy.next
