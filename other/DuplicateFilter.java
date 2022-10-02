import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.*;

public class DuplicateFilter {
    
    public static void main(String[] args) {
        try(
            BufferedReader br = new BufferedReader(new FileReader("test.txt"));
            BufferedWriter bw = new BufferedWriter(new FileWriter("movies.txt"))
            ) {
            String line;
            Set<String> addresses = new HashSet<>();
            List<String> hqporner = new ArrayList<>();
            List<String> goodporn = new ArrayList<>();
            List<String> pornwild = new ArrayList<>();
            List<String> milfnut = new ArrayList<>();
            List<String> pornhub = new ArrayList<>();
            List<String> other = new ArrayList<>();

            boolean commentBlock = false;

            while((line = br.readLine()) != null) {
                if(line.equals("")) bw.write("\n");
                else if(!addresses.contains(line)) {
                    bw.write(line + "\n");
                    addresses.add(line);
                }
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}