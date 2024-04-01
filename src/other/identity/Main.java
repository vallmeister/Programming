package other.identity;

public class Main {
    public static void main(String[] args) {
        final Point p1 = new Point(10, 10);
        final Point p2 = p1;
        final Point p3 = new Point(10, 10);
        System.out.println(p1 == p2);
        System.out.println(p1 == p3);
        System.out.println(p1.equals(p3));
    }
}
