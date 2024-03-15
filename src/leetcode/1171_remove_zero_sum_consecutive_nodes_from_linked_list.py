# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        prefix_sum = {0: sentinel}
        curr = sentinel.next
        prev = sentinel
        curr_sum = 0
        prev_nodes = {}
        while curr:
            prev_nodes[curr] = prev
            curr_sum += curr.val
            if curr_sum == 0:
                sentinel.next = curr.next
                curr = sentinel.next
                prev = sentinel
                prev_nodes = {}
                prefix_sum = {0: sentinel}
                curr_sum = 0
                continue
            elif curr_sum in prefix_sum:
                prev = prefix_sum[curr_sum]
                prev.next = curr.next
                prev, curr = sentinel, sentinel.next
                curr_sum = 0
                prev_nodes = {}
                prefix_sum = {0: sentinel}
                continue
            prefix_sum[curr_sum] = curr
            curr, prev = curr.next, curr
        return sentinel.next
