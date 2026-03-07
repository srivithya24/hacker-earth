import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            long n = sc.nextLong();
            // Consume the array elements even though they don't affect the result
            for (int i = 0; i < n; i++) {
                if (sc.hasNext()) sc.next();
            }
            // The condition is satisfied by all pairs (i, j) where i != j
            System.out.println(n * (n - 1));
        }
        sc.close();
    }
}
