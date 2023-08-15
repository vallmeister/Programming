# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        l1 = []
        l2 = []
        while head:
            if head.val < x:
                l1.append(head)
            else:
                l2.append(head)
            head = head.next
        l1 += l2
        for i in range(1, len(l1)):
            l1[i - 1].next = l1[i]
        l1[len(l1) - 1].next = None
        return l1[0]
