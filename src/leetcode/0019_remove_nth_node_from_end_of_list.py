from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


s = Solution()
ln5 = ListNode(5)
ln4 = ListNode(4, ln5)
ln3 = ListNode(3, ln4)
ln2 = ListNode(2, ln3)
ln1 = ListNode(1, ln2)
ln1 = s.removeNthFromEnd(ln1, 2)
while ln1:
    print(ln1.val)
    ln1 = ln1.next
ln1 = ListNode(1)
ln1 = s.removeNthFromEnd(ln1, 1)
while ln1:
    print(ln1.val)
    ln1 = ln1.next
ln2 = ListNode(2)
ln1 = ListNode(1, ln2)
ln1 = s.removeNthFromEnd(ln1, 1)
while ln1:
    print(ln1.val)
    ln1 = ln1.next
