package Coding.LeetCode;

import java.util.PriorityQueue;
import java.util.Queue;

public class KClosestPointsOrigin {

  public static int[][] kClosest(int[][] points, int k) {
    if (points.length == k) return points;
    int[][] solution = new int[k][2];
    if (k == 0) return solution;

    Queue<int[]> maxPriorityQueue = new PriorityQueue<>(k, (a,b) -> b[0] - a[0]);
    for (int i = 0; i < points.length; i++) {
      int[] point = points[i];
      int[] entry = {(int) (Math.pow(point[0], 2) + Math.pow(point[1], 2)), i};
      if (maxPriorityQueue.size() < k) maxPriorityQueue.add(entry);
      else if (entry[0] < maxPriorityQueue.peek()[0]) {
        maxPriorityQueue.poll();
        maxPriorityQueue.add(entry);
      }
    }
    for (int i = 0; i < k; i++) {
      int entryIndex = maxPriorityQueue.poll()[1];
      solution[i] = points[entryIndex];
    }
    return solution;
  }
}
