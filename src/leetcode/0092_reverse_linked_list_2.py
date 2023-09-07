# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(next=head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next, next_node.next, prev.next = next_node.next, prev.next, next_node
        return dummy.next


s = Solution()
five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
s.reverseBetween(one, 2, 4)
while one:
    print(one.val)
    one = one.next
second = ListNode(5)
first = ListNode(3, second)
s.reverseBetween(first, 1, 2)
while first:
    print(first.val)
    first = first.next
