package Coding.citadel;

import java.util.ArrayList;
import java.util.List;

public class GlobalMaximum {

  public static void main(String[] args) {
    List<Integer> list1 = new ArrayList<>();
    list1.add(2);
    list1.add(3);
    list1.add(5);
    list1.add(9);
    System.out.println(findMaximum(list1, 3));

  }

  public static int findMaximum(List<Integer> arr, int m) {
    List<List<Integer>> sequences = new ArrayList<>();
    getSequences(arr, m, 0, new ArrayList<Integer>(), sequences);
    return maximumMinimumDifference(sequences);
  }

  private static int maximumMinimumDifference(List<List<Integer>> sequences) {
    int globalMaximum = 0;
    for (List<Integer> sequence : sequences) {
      int currentMinimum = (int) Math.pow(10, 9) + 1;
      for (int i = 0; i < sequence.size() - 1; i++) {
        for (int j = i + 1; j < sequence.size(); j++) {
          int absoluteDifference = Math.abs(sequence.get(i) - sequence.get(j));
          if (absoluteDifference < currentMinimum) currentMinimum = absoluteDifference;
        }
      }
      if (currentMinimum > globalMaximum) globalMaximum = currentMinimum;
    }
    return globalMaximum;
  }

  private static void getSequences(List<Integer> superSet, int k, int idx, List<Integer> current,
                                   List<List<Integer>> solution) {
    if (current.size() == k) {
      solution.add(new ArrayList<>(current));
      return;
    }
    if (idx == superSet.size()) return;
    Integer x = superSet.get(idx);
    current.add(x);
    getSequences(superSet, k, idx+1, current, solution);
    current.remove(x);
    getSequences(superSet, k, idx+1, current, solution);
  }
}
