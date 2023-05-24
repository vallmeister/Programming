# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # TODO: Retry with sentinel bit
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        lst = stack.pop()
        carry = (lst.val + 1) // 10
        while stack and carry:
            lst.val = 0
            lst = stack.pop()
            carry = (lst.val + 1) // 10
        else:
            if not stack and carry:
                lst.val = 0
                head = ListNode(1, lst)
            else:
                lst.val += 1
        return head
