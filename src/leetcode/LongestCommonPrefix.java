package Coding.LeetCode;

import java.util.*;

public class LongestCommonPrefix {

    public static void main(String[] args) {
        String[] strings = {"flow", "flower", "flight"};
        System.out.println(sortedPrefix(strings));
    }

    /*
    My first idea to solve that problem.
    We sort the Strings lexicographically and take the longest common prefix of the first and last String. That must
    include the longest common prefix of all the Strings between those too.

    Runtime: O(n*log(n))
     */
    public static String sortedPrefix(String[] strs) {
        List<String> stringList = new ArrayList<>(Arrays.asList(strs));
        Collections.sort(stringList);
        String first = stringList.get(0);
        Collections.reverse(stringList);
        String last = stringList.get(0);

        String result = greatestCommonPrefix(first, last);

        return result;
    }

    /*
    Simply use the observation that LCP(s1,...,sn) = LCP(LCP(LCP(s1,s2),s3),...sn)
     */
    public static String horizontalScanning(String[] strs) {
        if (strs.length == 0) return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++)
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        return prefix;
    }

    /*
    Imagine a very short string is the common prefix at the end of the array. The above approach will still do S
    comparisons. One way to optimize this case is to do vertical scanning. We compare characters from top to bottom on
    the same column (same character index of the strings) before moving on to the next column.
    Time: O(S)
    Space: O(1)
     */
    public static String verticalScanning(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        for (int i = 0; i < strs[0].length() ; i++){
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j ++) {
                if (i == strs[j].length() || strs[j].charAt(i) != c)
                    return strs[0].substring(0, i);
            }
        }
        return strs[0];
    }

    private static String greatestCommonPrefix(String a, String b) {
        int minLength = Math.min(a.length(), b.length());
        for (int i = 0; i < minLength; i++) {
            if (a.charAt(i) != b.charAt(i)) {
                return a.substring(0, i);
            }
        }
        return a.substring(0, minLength);
    }
}
