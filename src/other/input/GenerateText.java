package other.input;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class GenerateText {

    static void generateTextFile() {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter("resources/output.txt", true))) {
            writer.write("Hello world!\n");
            writer.write("This is an example.\n");
            writer.write("Testing i/o.");
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }
}
