package Coding.LeetCode;

import java.util.ArrayList;
import java.util.List;

public class MinimumHeightTrees {

  public static void main(String[] args) {
    int n = 6;
    int[][] edges = {{3, 0}, {3, 1}, {3, 2}, {3, 4}, {5, 4}};
    System.out.println(findMinHeightTrees(n, edges));
  }

  public static List<Integer> findMinHeightTrees(int n, int[][] edges) {
    if (n == 1) {
      List<Integer> solution = new ArrayList<>(1);
      solution.add(0);
      return solution;
    }

    // manage neighbors of all nodes
    List<List<Integer>> neighborLists = new ArrayList<>(n);
    for (int i = 0; i < n; i++) neighborLists.add(new ArrayList<>());
    for (int[] edge : edges) {
      int start = edge[0];
      int end = edge[1];
      neighborLists.get(start).add(end);
      neighborLists.get(end).add(start);
    }

    List<Integer> leaves = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      if (neighborLists.get(i).size() == 1) leaves.add(i);
    }

    int centroids = n;

    while (centroids > 2) {
      centroids -= leaves.size();
      List<Integer> newLeaves = new ArrayList<>();

      for (Integer leave : leaves) {
        int neighbor = neighborLists.get(leave).get(0);
        neighborLists.get(neighbor).remove(leave);
        if (neighborLists.get(neighbor).size() == 1) newLeaves.add(neighbor);
      }
      leaves = newLeaves;
    }
    return leaves;
  }
}
