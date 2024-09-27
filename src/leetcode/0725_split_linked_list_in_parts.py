# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        n = self.get_length(head)
        for _ in range(k):
            sentinal = ListNode()
            prev = sentinal
            sentinal.next = head
            for _ in range(n // k + (1 if len(ans) < n % k else 0)):
                head = head.next
                prev = prev.next
            prev.next = None
            ans.append(sentinal.next)

        return ans
    
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
