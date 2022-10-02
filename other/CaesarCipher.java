public class CaesarCipher {

  private static final int UPPERCASE_OFFSET = 65; // ASCII for 'A'
  private static final int LOWERCASE_OFFSET = 97; // ASCII for 'a'

  public static void main(String[] args) {
    System.out.println("Encoding \"innoWake rules\": "
            + encode("innoWake rules", 9));
    System.out.println("Decoding \"IUHUR\": "
            + decode("IUHUR", 6));
  }

  public static String encode(String plaintext, int rotations) {
    int length = plaintext.length();
    StringBuilder cipherBuilder = new StringBuilder(length);

    for (int i = 0; i < length; i++) {
      char current = plaintext.charAt(i);

      if (!Character.isLetter(current) || current > 127) {
        cipherBuilder.append(current);
        continue;
      }

      if (Character.isUpperCase(current)) {
        current -= UPPERCASE_OFFSET;
        current += rotations;
        current %= 26;
        current += UPPERCASE_OFFSET;

        cipherBuilder.append(current);
      } else {
        current -= LOWERCASE_OFFSET;
        current += rotations;
        current %= 26;
        current += LOWERCASE_OFFSET;

        cipherBuilder.append(current);
      }
    }
    return cipherBuilder.toString();
  }

  public static String decode(String ciphertext, int rotations) {
    int length = ciphertext.length();
    StringBuilder plaintextBuilder = new StringBuilder(length);

    for (int i = 0; i < length; i++) {
      char current = ciphertext.charAt(i);

      if (!Character.isLetter(current) || current > 127) { // Not affecting characters that aren't in ASCII table
        plaintextBuilder.append(current);
        continue;
      }

      if (Character.isUpperCase(current)) {
        current -= UPPERCASE_OFFSET;
        current += 26; // prevent negative result
        current -= rotations;
        current %= 26;
        current += UPPERCASE_OFFSET;

        plaintextBuilder.append(current);
      } else {
        current -= LOWERCASE_OFFSET;
        current += 26;
        current -= rotations;
        current %= 26;
        current += LOWERCASE_OFFSET;

        plaintextBuilder.append(current);
      }
    }
    return plaintextBuilder.toString();
  }

  // Came up with that idea after finishing the decode method from above
  private static String decodeAlternatively(String ciphertext, int rotations) {
    rotations %= 26; // avoiding negative rotations
    return encode(ciphertext, 26 - rotations);
  }
}
