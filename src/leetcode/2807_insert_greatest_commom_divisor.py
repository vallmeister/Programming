# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            gcd_val = self.gcd(curr.val, curr.next.val)
            gcd_node = ListNode(gcd_val, curr.next)
            curr.next = gcd_node
            curr = curr.next.next
        return head

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
