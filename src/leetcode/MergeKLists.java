package Coding.LeetCode;

import Coding.LeetCode.util.ListNode;

import java.util.*;

public class MergeKLists {
  public static ListNode mergeKListsSimple(ListNode[] lists) {
    ListNode mergedList = new ListNode(Integer.MAX_VALUE);
    ListNode iterator = new ListNode(Integer.MAX_VALUE);;
    int nonEmptyLists = lists.length;

    while(nonEmptyLists > 0) {
      nonEmptyLists = 0;
      int smallestValue = Integer.MAX_VALUE;
      int nextIndex = 0;

      // Find smallest value
      for (int i = 0; i < lists.length; i++) {
        ListNode temp = lists[i];

        if (temp != null) {
          nonEmptyLists++;
          if (temp.val <= smallestValue) {
            smallestValue = temp.val;
            nextIndex = i;
          }
        }
      }
      if (nonEmptyLists == 0) break;
      if (mergedList.val != Integer.MAX_VALUE) {
        iterator.next = lists[nextIndex];
        iterator = iterator.next;
        lists[nextIndex] = lists[nextIndex].next;
      } else {
        mergedList = lists[nextIndex];
        iterator = mergedList;
        lists[nextIndex] = lists[nextIndex].next;
      }
    }

    if (iterator.val != Integer.MAX_VALUE) iterator.next = null;
    else mergedList = null;
    return mergedList;
  }

  public static ListNode mergeKListsWithPriorityQueue(ListNode[] lists) {
    ListNode mergedList = new ListNode();
    PriorityQueue<Integer> valueQueue = new PriorityQueue<>();
    Map<Integer, ListNode> listNodeStartingWith = new HashMap<>(lists.length);


    return mergedList;
  }
}
