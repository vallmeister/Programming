from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        prev = sentinel
        curr = sentinel.next
        stack = []
        while curr:
            fst = curr
            for _ in range(k):
                if not curr:
                    break
                stack.append(curr)
                curr = curr.next
            else:
                while stack:
                    prev.next = stack.pop()
                    prev = prev.next
                prev.next = None
                continue
            prev.next = fst
        return sentinel.next


s = Solution()
five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
head = ListNode(1, two)
head = s.reverseKGroup(head, 2)
while head:
    print(head.val)
    head = head.next

two = ListNode(2)
head = ListNode(1, two)
head = s.reverseKGroup(head, 2)
while head:
    print(head.val)
    head = head.next
