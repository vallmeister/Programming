package Coding.LeetCode.lc75.level01;

import java.util.HashMap;
import java.util.Map;

public class IsomorphicStrings {

    public static void main(String[] args) {
        System.out.println(isIsomorphic("egg", "add"));
        System.out.println(isIsomorphic("foo", "bar"));
        System.out.println(isIsomorphic("paper", "title"));
        System.out.println(isIsomorphic("bbbaaaba", "aaabbbba"));
    }

    /* Idea: A String is isomorphic iff  the number of different letters in s and t is equal and for each letter
            occurring k times in s there is a letter in t also occurring k times.
     */
    public static boolean isIsomorphic(String s, String t) {
        Map<String, String> sToT = new HashMap<>();
        Map<String, String> tToS = new HashMap<>();

        return true;
    }
}
