class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """ 2 pointer search"""
    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    """ Unefficient, 1st solution """
    def has_cycle_helper(self, head, visited) -> bool:
        if head is None:
            return False
        if head.val in visited:
            return True
        visited.add(head.val)
        return self.has_cycle_helper(head.next, visited)
