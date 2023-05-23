# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next:
            for _ in range(m):
                if not curr.next:
                    break
                curr = curr.next
            for _ in range(n):
                if not curr.next:
                    break
                curr.next = curr.next.next
        return dummy.next
