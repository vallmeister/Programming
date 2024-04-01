package other.functional;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) {
        /* Inner class */
        class TrimmingComparator implements Comparator<String> {
            @Override
            public int compare(String s1, String s2) {
                return s1.trim().compareTo(s2.trim());
            }
        }
        String[] words = {"M", "\nSkyfall", "Q", "\t\tAdele\t"};
        Arrays.sort(words);
        System.out.println(Arrays.toString(words));
        Arrays.sort(words, new TrimmingComparator());
        System.out.println(Arrays.toString(words));

        /* Inner anonymous class */
        Arrays.sort(words, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.trim().compareTo(o2.trim());
            }
        });
        System.out.println(Arrays.toString(words));

        /* Lambda */
        Arrays.sort(words,
                (String s1, String s2) -> {
                    return s1.trim().compareTo(s2.trim());
                });
        Comparator<String> c = (String s1, String s2) -> {
            return s1.trim().compareTo(s2.trim());
        };

        /* Streams */
        System.out.println(
                Stream.of(-4, 1, -2, 3)
                        .map(Math::abs).sorted().collect(Collectors.toList())
        );
        List<Integer> range = IntStream.range(1, 10).boxed().toList();
        Predicate<Integer> isEven = i -> i % 2 == 0;
        range.stream().filter(isEven).forEach(System.out::println);
        int[] numbers = new int[]{8, 1, 9, 3, 6, 7, 11, 2, 0};
        System.out.println(range.stream().filter(isEven).sorted(Collections.reverseOrder()).collect(Collectors.toList()));
        System.out.println(range.stream().max(Comparator.naturalOrder()).get());
        System.out.println(range.stream().min(Comparator.naturalOrder()).get());
        System.out.println(range.stream().count());
        System.out.println(range.stream().reduce(0, Integer::sum));
    }
}
