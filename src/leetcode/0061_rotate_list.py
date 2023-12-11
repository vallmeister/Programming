# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        n = 0
        curr = dummy.next
        while curr:
            n += 1
            curr = curr.next
        if n == 0:
            return head
        k %= n
        if k == 0:
            return head
        start = dummy.next
        prev = dummy
        for _ in range(n - k):
            prev, start = start, start.next
        prev.next = None
        tmp = dummy.next
        dummy.next = start
        curr = dummy
        for _ in range(k):
            curr = curr.next
        curr.next = tmp
        return dummy.next


s = Solution()
five = ListNode(5)
four = ListNode(4, next=five)
three = ListNode(3, next=four)
two = ListNode(2, next=three)
head = ListNode(1, next=two)
head = s.rotateRight(head, 2)
while head:
    print(head.val)
    head = head.next
