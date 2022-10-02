package Coding.LeetCode;

import Coding.LeetCode.util.ListNode;

import java.util.ArrayDeque;

public class ReorderList {
  public static void main(String[] args) {
    ListNode listNode = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
    reorderList(listNode);
    System.out.println(listNode);
  }

  public static void reorderList(ListNode head) {
    if (head.next == null) return;
    ArrayDeque<ListNode> nodes = new ArrayDeque<>();
    ListNode current = head;
    while (current.next != null) {
      current = current.next;
      nodes.add(current);
    }
    current = head;
    boolean front = false;

    while (!nodes.isEmpty()) {
      current.next = front ? nodes.pollFirst() : nodes.pollLast();
      current = current.next;
      front = !front;
    }
    current.next = null;
  }
}
