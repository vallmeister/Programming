import java.util.List;

class Solution {
    int answer;
    boolean[] visited;
    int m;
    int n;

    public int assignBikes(int[][] workers, int[][] bikes) {
        answer = Integer.MAX_VALUE;
        m = workers.length;
        n = bikes.length;
        visited = new boolean[n];
        backtracking(0, 0, workers, bikes);
        return answer;
    }

    private void backtracking(int worker, int distance, int[][] workers, int[][] bikes) {
        if (worker == m) {
            answer = Math.min(answer, distance);
            return;
        } else if (distance >= answer) {
            return;
        }
        int x0 = workers[worker][0];
        int y0 = workers[worker][1];
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            int x1 = bikes[i][0];
            int y1 = bikes[i][1];
            visited[i] = true;
            backtracking(worker + 1, distance + Math.abs(x1 - x0) + Math.abs(y1 - y0), workers, bikes);
            visited[i] = false;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.assignBikes(new int[][]{{0,0}, {2,1}}, new int[][]{{1,2},{3,3}}));
        System.out.println(s.assignBikes(new int[][]{{0,0}, {1,1}, {2,0}}, new int[][]{{1,0},{2,2}, {2,1}}));
        System.out.println(s.assignBikes(new int[][]{{0,0}, {1,0}, {2,0}, {3,0}, {4,0}}, new int[][]{{0,999},{1,999},{2,999},{3,999},{4,999}}));
    }
}