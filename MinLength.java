import java.util.*;

class TestClass {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            for (int i = 0; i < n; i++) b[i] = sc.nextInt();

            int start = 0;
            while (start < n && a[start] == b[start]) {
                start++;
            }

            if (start == n) {
                System.out.println(0);
                continue;
            }

            int end = n - 1;
            while (end >= 0 && a[end] == b[end]) {
                end--;
            }

            System.out.println(end - start + 1);
        }
    }
}
