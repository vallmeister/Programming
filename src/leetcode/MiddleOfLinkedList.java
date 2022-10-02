package Coding.LeetCode;

import Coding.LeetCode.util.ListNode;

public class MiddleOfLinkedList {

  public static ListNode middleNode(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while (fast.next != null) {
      slow = slow.next;
      fast = fast.next;
      if (fast.next == null) break;
      fast = fast.next;
    }
    return slow;
  }
}
