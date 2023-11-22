# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sequence = []
        while head:
            sequence.append(head.val)
            head = head.next
        i = 0
        j = len(sequence) - 1
        while i < j:
            if sequence[i] != sequence[j]:
                return False
            i += 1
            j -= 1
        return True
