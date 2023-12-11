# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0, next=head)
        new_dummy = Node(0)
        curr = dummy.next
        new_prev = new_dummy
        old_to_new = {}
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            new_prev.next = new_node
            curr = curr.next
            new_prev = new_prev.next
        curr = dummy.next
        while curr:
            if curr.random:
                new_node = old_to_new[curr]
                new_node.random = old_to_new[curr.random]
            curr = curr.next

        return new_dummy.next
