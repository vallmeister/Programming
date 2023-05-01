from typing import Optional
import pprint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


s = Solution()
ln5 = ListNode(5)
ln4 = ListNode(4, ln5)
ln3 = ListNode(3, ln4)
ln2 = ListNode(2, ln3)
ln1 = ListNode(1, ln2)
pprint.pprint(s.middleNode(ln1).val)
ln6 = ListNode(6)
ln5 = ListNode(5, ln6)
ln4 = ListNode(4, ln5)
ln3 = ListNode(3, ln4)
ln2 = ListNode(2, ln3)
ln1 = ListNode(1, ln2)
pprint.pprint(s.middleNode(ln1).val)
