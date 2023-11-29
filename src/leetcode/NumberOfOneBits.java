public class NumberOfOneBits {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        while (n != 0) {
            ans += 1 & n;
            n >>>= 1;
            System.err.println(n);
        }
        return ans;
    }

    public static void main(String[] args) {
        NumberOfOneBits solution = new NumberOfOneBits();
        System.out.println(solution.hammingWeight(11));
    }
}
