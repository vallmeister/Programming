# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [head for head in lists if head]

        def merge_two_sorted_lists(head1, head2):
            sentinel = ListNode()
            curr = sentinel
            while head1 or head2:
                if head1 and head2:
                    if head1.val < head2.val:
                        curr.next = head1
                        head1 = head1.next
                    else:
                        curr.next = head2
                        head2 = head2.next
                elif head1:
                    curr.next = head1
                    head1 = head1.next
                elif head2:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            curr.next = None
            return sentinel.next

        def divide_and_conquer(list_of_lists):
            n = len(list_of_lists)
            if n == 1:
                return list_of_lists.pop()
            elif n == 2:
                head1, head2 = list_of_lists
                return merge_two_sorted_lists(head1, head2)
            else:
                sorted_1 = divide_and_conquer(list_of_lists[:n // 2])
                sorted_2 = divide_and_conquer(list_of_lists[n // 2:])
                return merge_two_sorted_lists(sorted_1, sorted_2)

        if not lists:
            return None
        return divide_and_conquer(lists)
