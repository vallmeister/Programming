# Definition for singly-linked list.
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = defaultdict(int)
        while head:
            counter[head.val] += 1
            head = head.next
        sentinel = ListNode()
        curr = sentinel
        for v in counter.values():
            curr.next = ListNode(v)
            curr = curr.next
        return sentinel.next
