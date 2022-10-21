package Programming.uva_judge;

import java.util.*;

public class Borrowers_230 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    List<String> books = new ArrayList<>();
    String book = "";
    while (!(book = sc.nextLine()).equals("END")) {
      String[] titleAndAuthor = book.split("by");
      book = titleAndAuthor[1] + "---" + titleAndAuthor[0].replace("\"", "");
      books.add(book);
    }
    Collections.sort(books);
    boolean[] borrowed = new boolean[books.size()];
    Map<String, Integer> booktitlePosition = new HashMap<>();
    for (int i = 0; i < books.size(); i++) {
      booktitlePosition.put(books.get(i).split("---")[1].trim(), i);
    }
    List<String> shelve = new ArrayList<>();
    String operation = "";
    while (!(operation = sc.nextLine()).equals("END")) {
      if (operation.startsWith("BORROW")) {
        String titl1 = operation.replace("\"", "").replaceAll("BORROW ", "");
        borrowed[(int) booktitlePosition.get(titl1)] = true;
      } else if (operation.startsWith("RETURN")) {
        shelve.add(operation.replace("\"", "").replaceAll("RETURN ", ""));
      } else if (operation.startsWith("SHELVE")) {
        for (String title : shelve) {
          int index = booktitlePosition.get(title);
          while (index >= 0 && !borrowed[index--]);
          if (index < 0) System.out.printf("Put %s first", title);
          else {
            String title2 = books.get(index).split("---")[1];
            System.out.printf("Put %s after %s%n", title, title2);
          }
          borrowed[booktitlePosition.get(title)] = false;
          shelve = new ArrayList<>();
        }
      }
    }
    System.out.println("END");
  }
}
