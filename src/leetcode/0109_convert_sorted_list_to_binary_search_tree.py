# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if prev:
            prev.next = None
        if head != slow:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
