package Coding.citadel;

import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;

public class PrimeFactorVisitation {
  public static void main(String[] args) {
    System.out.println(primeFactors(12));
  }

  public static List<Integer> lightBulbs(List<Integer> states, List<Integer> numbers) {
    int[] lightBulbArray = new int[states.size()];
    for (int number : numbers) {
      List<Integer> primes = primeFactors(number);
      for (int prime : primes) {
        int index = prime - 1;
        while (index < states.size()) {
          lightBulbArray[index] += 1;
          index += prime;
        }
      }
    }
    for (int i = 0; i < states.size(); i++) {
      if (lightBulbArray[i] % 2 == 1) {
        int state = 1 - states.get(i);
        states.set(i, state);
      }
    }
    return states;
  }

  public static List<Integer> primeFactors(int numbers) {
    int n = numbers;
    List<Integer> factors = new ArrayList<Integer>();
    for (int i = 2; i <= n / i; i++) {
      while (n % i == 0) {
        factors.add(i);
        n /= i;
      }
    }
    if (n > 1) {
      factors.add(n);
    }
    Set<Integer> uniqueFactors = new HashSet<>(factors);
    return new ArrayList<>(uniqueFactors);
  }
}
