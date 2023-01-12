class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Intuitive solution. Fast, but requires O(n) space.
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodesA = set()
        while headA is not None:
            nodesA.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in nodesA:
                return headB
            headB = headB.next
        return None

    """
    Space-efficient solution: Simulating concatenation of both lists and waiting for both pointers to meet. If they 
    don't meet but both are None, we know that there's no intersection.
    """
    def get_intersection_node_efficiently(self, head_a, head_b):
        node_a = head_a
        node_b = head_b
        while node_a != node_b:
            node_a = head_b if node_a is None else node_a.next
            node_b = head_a if node_b is None else node_b.next
        return node_a
