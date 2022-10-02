package Programming.google.codejam.cj_19.qualification;

import java.math.BigInteger;
import java.util.Scanner;

public class ForegoneSolution {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int test = 1; test <= t; test++) {
      BigInteger n = new BigInteger(sc.next());
      BigInteger a = BigInteger.ZERO;
      BigInteger b = BigInteger.ZERO;

      int exponent = 0;
      while (n.compareTo(BigInteger.ZERO) > 0) {
        int digit = n.mod(BigInteger.TEN).intValue();
        if (digit == 4) {
          a = a.add(BigInteger.TWO.multiply(BigInteger.TEN.pow(exponent)));
          b = b.add(BigInteger.TWO.multiply(BigInteger.TEN.pow(exponent)));
        } else {
          a = a.add((new BigInteger("" + digit)).multiply(BigInteger.TEN.pow(exponent)));
        }
        exponent++;
        n = n.divide(BigInteger.TEN);
      }

      System.out.format("Case #%d: %s %s%n", test, a.toString(), b.toString());
    }
  }
}
