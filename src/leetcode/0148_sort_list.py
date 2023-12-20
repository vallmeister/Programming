# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        mid = self.get_mid(head)
        if head == mid:
            return head
        head = self.sortList(head)
        mid = self.sortList(mid)
        sentinel = ListNode()
        curr = sentinel
        while head or mid:
            if head and mid:
                if head.val < mid.val:
                    curr.next = head
                    head = head.next
                else:
                    curr.next = mid
                    mid = mid.next
            elif head:
                curr.next = head
                head = head.next
            elif mid:
                curr.next = mid
                mid = mid.next
            curr = curr.next
        curr.next = None
        return sentinel.next

    def get_mid(self, head):
        if not head:
            return None
        sentinel = ListNode(next=head)
        slow = sentinel
        fast = sentinel
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            prev, slow = slow, slow.next
        if prev:
            prev.next = None

        return slow


s = Solution()
zero = ListNode(0)
four = ListNode(4, zero)
three = ListNode(3, four)
five = ListNode(5, three)
head = ListNode(-1, five)
head = s.sortList(head)
while head:
    print(head.val)
    head = head.next
