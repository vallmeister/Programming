package other.input;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        GenerateText.generateTextFile();

        try(BufferedReader reader = new BufferedReader(new FileReader("resources/output.txt"))) {
            for (String line: reader.lines().toList()) {
                System.out.println(line);
            }
        } catch (IOException exception) {
            exception.printStackTrace();
        } finally {
            System.out.println("Finally");
        }
        System.out.printf("%.2f\n", 20f);
        System.out.printf("%03d\n", 20);
    }
}
