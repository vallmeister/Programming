package leetcode;

import java.util.List;

public class MaximumDistanceInArrays {
    public int maxDistance(List<List<Integer>> arrays) {
        int dist = 0;
        int m = arrays.size();

        List<Integer> currList = arrays.get(0);
        int n = currList.size();
        int currMin = currList.get(0);
        int currMax = currList.get(n - 1);

        for (int i = 1; i < m; i++) {
            currList = arrays.get(i);
            n = currList.size();
            final int fst = currList.get(0);
            final int lst = currList.get(n - 1);
            dist = Math.max(dist, currMax - fst);
            dist = Math.max(dist, lst - currMin);
            currMax = Math.max(currMax, lst);
            currMin = Math.min(currMin, fst);
        }
        return dist;
    }
}
