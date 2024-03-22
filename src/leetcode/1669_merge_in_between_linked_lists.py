# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        curr = list1
        for _ in range(a):
            prev, curr = curr, curr.next
        prev.next = list2
        for _ in range(b - a + 1):
            curr = curr.next
        while prev.next:
            prev = prev.next
        prev.next = curr
        return list1
