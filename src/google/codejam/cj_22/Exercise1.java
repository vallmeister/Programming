package Coding.codeJam.cj22;

import java.util.*;

public class Exercise1 {
    private static final String IMPOSSIBLE = "IMPOSSIBLE";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testcases = scanner.nextInt();

        for (int testcase = 1; testcase <= testcases; testcase++) {
            int n = scanner.nextInt();
            List<String> towers = new ArrayList<>(n);
            boolean valid = true;
            for (int i = 0; i < n; i++) {
                String tower = scanner.next();
                if (isTowerValid(tower)) towers.add(tower);
                else valid = false;
            }
            if (!valid) {
                System.out.format("Case #%d: %s\n", testcase, IMPOSSIBLE);
                continue;
            }

            MERGE: for (int i = 0; i < n; i++) {
                if (consistsOfOneLetterOnly(towers.get(i))) {
                    String tower = towers.remove(i);
                    if (tower.length() == 0) continue;
                    char single = tower.charAt(0);
                    for (int j = 0; j < towers.size(); j++) {
                        String tmp = towers.get(j);
                        if (tmp.length() == 0) continue;
                        char first = tmp.charAt(0);
                        char last = tmp.charAt(tmp.length() - 1);
                        if (first == single) {
                            towers.add(i, "");
                            towers.remove(tmp);
                            tmp = tower + tmp;
                            towers.add(j, tmp);
                            continue MERGE;
                        } else if (last == single) {
                            towers.add(i, "");
                            towers.remove(tmp);
                            tmp += tower;
                            towers.add(j, tmp);
                            continue MERGE;
                        }
                    }
                    towers.add(i, tower);
                }
            }
            towers.removeAll(List.of(""));
            String solution = towers.remove(0);
            SOLUTION: while (!towers.isEmpty()) {
                char first = solution.charAt(0);
                char last = solution.charAt(solution.length() - 1);
                for (int i = 0; i < towers.size(); i++) {
                    String tower = towers.get(i);
                    if (tower.length() == 0) continue;
                    if (last == tower.charAt(0)) {
                        solution += tower;
                        towers.remove(tower);
                        continue SOLUTION;
                    } else if (first == tower.charAt(tower.length() - 1)) {
                        solution = tower + solution;
                        towers.remove(tower);
                        continue SOLUTION;
                    }
                }
                solution += towers.remove(0);
            }
            solution = isTowerValid(solution) ? solution : IMPOSSIBLE;

            System.out.format("Case #%d: %s\n", testcase, solution);
        }
    }

    private static boolean isTowerValid(String string) {
        for (int i = 0; i < string.length() - 1; i++) {
            for (int j = i + 1; j < string.length(); j++) {
                char current = string.charAt(i);
                if (current == string.charAt(j)) {
                    String substring = string.substring(i, j + 1);
                    for (int k = 0; k < substring.length(); k++) if (substring.charAt(k) != current) return false;
                }
            }
        }
        return true;
    }
    private static boolean consistsOfOneLetterOnly(String string) {
        Set<Character> characterSet = new HashSet<>();
        for (int i = 0; i < string.length(); i++) characterSet.add(string.charAt(i));
        return characterSet.size() == 1;
    }
}
