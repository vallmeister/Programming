package Coding.LeetCode;

import Coding.LeetCode.util.ListNode;

public class MergeTwoSortedLists {

  public static void main(String[] args) {
    ListNode listNode1 = null;
    ListNode listNode2 = null;
    ListNode listNode3 = new ListNode(3, new ListNode(5, new ListNode(9, null)));
    ListNode listNode4 = new ListNode(4, new ListNode(10, null));

    System.out.println(mergeTwoLists(listNode1, listNode2));
    System.out.println(mergeTwoLists(listNode1, listNode3));
    System.out.println(mergeTwoLists(listNode4, listNode2));
    System.out.println(mergeTwoLists(listNode3, listNode4));
  }

  /*
  Own idea: Merge the two lists like the join part of merge sort.
  Time: O(n+m)
  Space: O(1)
   */
  private static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    if (list1 == null) return list2;
    else if (list2 == null) return list1;

    ListNode mergedListHead;
    ListNode mergedNext;

    if (list1.val < list2.val) {
      mergedListHead = list1;
      list1 = list1.next;
    } else {
      mergedListHead = list2;
      list2 = list2.next;
    }
    mergedNext = mergedListHead;

    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        mergedNext.next = list1;
        mergedNext = mergedNext.next;
        list1 = list1.next;
      } else {
        mergedNext.next = list2;
        mergedNext = mergedNext.next;
        list2 = list2.next;
      }
    }
    if (list1 == null && list2 != null) mergedNext.next = list2;
    else if (list2 == null && list1 != null) mergedNext.next = list1;

    return mergedListHead;
  }

}
