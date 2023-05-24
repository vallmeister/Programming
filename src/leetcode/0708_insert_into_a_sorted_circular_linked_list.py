# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    # TODO: Try again with 2 pointers
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        elif head.next == head:
            head.next = Node(insertVal, head)
            return head
        curr = head
        while curr.next:
            if curr.val <= insertVal <= curr.next.val:
                insert_node = Node(insertVal, curr.next)
                curr.next = insert_node
                return head

            elif curr.next == head.next:
                curr.next = Node(insertVal, head)
                return head
            curr = curr.next
        return head


s = Solution()
one = Node(1)
four = Node(4, one)
head = Node(3, four)
one.next = head
print(s.insert(head, 2))
print(s.insert(None, 1))
head = Node(1)
print(s.insert(head, 0))
