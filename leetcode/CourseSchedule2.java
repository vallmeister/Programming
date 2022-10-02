package Coding.LeetCode;

import java.util.*;

public class CourseSchedule2 {

  public static void main(String[] args) {
    int[][] prerequesites = {{1, 0}, {2, 0}, {3, 1}, {3, 2}, {2, 3}};
    System.out.println(Arrays.toString(findOrder(4, prerequesites)));

  }

  public static int[] findOrder(int numCourses, int[][] prerequisites) {
    if (numCourses == 1) return new int[1];
    int[] solution = new int[numCourses];
    if (prerequisites.length == 0) {
      for (int i = 0; i < numCourses; i++) solution[i] = i;
      return solution;
    }
    List<Set<Integer>> childrenList = new ArrayList<>(numCourses);
    for (int i = 0; i < numCourses; i++) childrenList.add(new HashSet<>());
    for (int[] prerequisite : prerequisites) childrenList.get(prerequisite[1]).add(prerequisite[0]);
    Set<Integer> scheduledCourses = new HashSet<>(numCourses);

    int n = numCourses;
    int position = numCourses - 1;
    while (n > 0) {
      int leaves = 0;
      for (int i = 0; i < numCourses; i++) {
        if (scheduledCourses.contains(i)) continue;
        Set<Integer> ithChildren = childrenList.get(i);
        if (ithChildren.size() == 0) {
          scheduledCourses.add(i);
          leaves++;
          n--;
          solution[position] = i;
          position--;
          for (Set<Integer> children : childrenList) children.remove(i);
        }
      }
      if (leaves == 0) return new int[0];
    }
    return solution;
  }
}
