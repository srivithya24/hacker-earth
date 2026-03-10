import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        FastReader fr = new FastReader();
        String tStr = fr.next();
        if (tStr == null) return;
        
        int t = Integer.parseInt(tStr);
        while (t-- > 0) {
            int n = fr.nextInt();
            long totalSum = 0;
            long positiveSum = 0;
            long negativeCapacity = 0;
            
            for (int i = 0; i < n; i++) {
                long val = fr.nextLong();
                totalSum += val;
                if (val > 0) {
                    positiveSum += val;
                } else if (val < 0) {
                    // How many '+2's this index can take before turning positive
                    negativeCapacity += Math.abs(val) / 2;
                }
            }
            
            // Logic: 
            // 1. Total sum must be <= 0 so that adding 1 per op can reach 0.
            // 2. We must have enough negative 'room' to dump the +2 part of the ops
            //    required to clear the positive numbers.
            if (totalSum <= 0 && positiveSum <= negativeCapacity) {
                System.out.println(-totalSum);
            } else {
                System.out.println("-1");
            }
        }
    }

    // Fast I/O for large constraints
    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String s = br.readLine();
                    if (s == null) return null;
                    st = new StringTokenizer(s);
                } catch (IOException e) { return null; }
            }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
        long nextLong() { return Long.parseLong(next()); }
    }
}
