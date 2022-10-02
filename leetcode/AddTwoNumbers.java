package Coding.LeetCode;

import Coding.LeetCode.util.ListNode;

public class AddTwoNumbers {

  public static void main(String[] args) {
    ListNode listNode1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    ListNode listNode2 = new ListNode(5, new ListNode(6, new ListNode(4)));
    ListNode listNode3 = new ListNode(3, new ListNode(5, new ListNode(9, null)));
    ListNode listNode4 = new ListNode(4, new ListNode(10, null));
    ListNode listNode5 = new ListNode(0);
    ListNode listNode6 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));
    ListNode listNode7 = new ListNode(9, new ListNode(8));
    ListNode listNode8 = new ListNode(0);

    System.out.println(addTwoNumbers(listNode1, listNode2));
    System.out.println(addTwoNumbers(listNode5, listNode8));
    System.out.println(addTwoNumbers(listNode6, listNode7));
  }

  /*
  Own idea. Iterate through both lists and add the numbers. Save the carry bit and don't stop until both lists are done.
   */
  public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int sum = l1.val + l2.val;
    ListNode result = new ListNode(sum % 10);
    int carry = sum / 10;
    ListNode currentNode = result;
    l1 = l1.next;
    l2 = l2.next;

    while (l1 != null || l2 != null) {
      int first = l1 != null ? l1.val : 0;
      int second = l2 != null ? l2.val : 0;

      sum = first + second + carry;
      currentNode.next = new ListNode(sum % 10);
      carry = sum / 10;
      currentNode = currentNode.next;
      if (l1 != null) l1 = l1.next;
      if (l2 != null) l2 = l2.next;
    }

    if (carry > 0) currentNode.next = new ListNode(carry);
    return result;
  }
}
