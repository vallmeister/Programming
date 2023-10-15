from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(next=head)
        curr = dummy

        def gcd(a, b):
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a < b:
                return gcd(b, a)
            return gcd(b, a % b)

        while curr.next:
            divisor = gcd(curr.val, curr.next.val)
            curr.next = ListNode(divisor, curr.next)
            curr = curr.next.next
        return dummy.next
