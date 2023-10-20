# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = prev.next
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt
            prev = curr
            curr = curr.next
        return dummy.next


s = Solution()
