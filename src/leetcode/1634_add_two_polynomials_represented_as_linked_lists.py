# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head = PolyNode()
        curr = head
        while poly1 or poly2:
            if poly1 and poly2 and poly1.power > poly2.power or poly1 and not poly2:
                nxt = PolyNode(poly1.coefficient, poly1.power)
                curr.next = nxt
                poly1 = poly1.next
            elif poly1 and poly2 and poly1.power < poly2.power or not poly1 and poly2:
                nxt = PolyNode(poly2.coefficient, poly2.power)
                curr.next = nxt
                poly2 = poly2.next
            elif poly1 and poly2 and poly1.power == poly2.power and poly1.coefficient + poly2.coefficient == 0:
                poly1 = poly1.next
                poly2 = poly2.next
                continue
            elif poly1 and poly2 and poly1.power == poly2.power:
                nxt = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                curr.next = nxt
                poly1 = poly1.next
                poly2 = poly2.next
            curr = curr.next
        return head.next


def build_linked_list(nodes):
    head = PolyNode()
    curr = head
    for coefficient, power in nodes:
        nxt = PolyNode(coefficient, power)
        curr.next = nxt
        curr = curr.next
    return head.next


s = Solution()
p1 = build_linked_list([[1, 1]])
p2 = build_linked_list([[1, 0]])
ps = s.addPoly(p1, p2)
while ps:
    print(f'{ps.coefficient}x^{ps.power}')
    ps = ps.next

p1 = build_linked_list([[2, 2], [4, 1], [3, 0]])
p2 = build_linked_list([[3, 2], [-4, 1], [-1, 0]])
ps = s.addPoly(p1, p2)
while ps:
    print(f'{ps.coefficient}x^{ps.power}')
    ps = ps.next
