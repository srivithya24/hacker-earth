import java.util.*;
import java.util.regex.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());

        String regex =
                "^(?=.{1,253}$)(?!-)(?:[A-Za-z0-9]" +
                "(?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\\.)+" +
                "[A-Za-z]{2,}$";

        Pattern pattern = Pattern.compile(regex);

        for (int i = 0; i < t; i++) {

            String domain = sc.nextLine().trim();

            if (pattern.matcher(domain).matches()) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }
        }

        sc.close();
    }
}
