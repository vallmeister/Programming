# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = True

        # find start of 2nd half
        sentinel = ListNode(next=head)
        slow = sentinel
        fast = sentinel
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse list in-place
        def reverse(ls):
            curr = ls
            prev = None
            while curr:
                tmp_next = curr.next
                curr.next = prev
                prev = curr
                curr = tmp_next
            return prev

        tail = reverse(slow.next)
        second_half = tail
        first_half = head

        # prev now is the head of our reversed 2nd half
        while first_half and tail:
            if head.val != tail.val:
                ans = False
            first_half = first_half.next
            tail = tail.next
        reverse(second_half)
        return ans


head = ListNode(1, ListNode(2, ListNode(2, ListNode(5))))
print(Solution().isPalindrome(head))
while head:
    print(head.val)
    head = head.next
