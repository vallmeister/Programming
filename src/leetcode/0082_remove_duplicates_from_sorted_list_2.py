# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy.next
        visited = set()
        duplicates = set()
        while curr:
            if curr.val in visited:
                duplicates.add(curr.val)
            visited.add(curr.val)
            curr = curr.next
        prev = dummy
        curr = dummy.next
        while curr:
            if curr.val not in duplicates:
                prev.next = curr
                prev = prev.next
            else:
                prev.next = None
            curr = curr.next
        return dummy.next


s = Solution()
snd = ListNode(1)
fst = ListNode(1, snd)
s.deleteDuplicates(fst)
