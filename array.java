import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Using BufferedReader for faster input handling
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N
        String line1 = br.readLine();
        if (line1 == null) return;
        int n = Integer.parseInt(line1.trim());
        
        // Read the array elements
        String[] elements = br.readLine().split("\\s+");
        
        // Map to store frequencies of (A[i] - i)
        // Key: the value of (A[i] - i), Value: how many times it appears
        Map<Integer, Long> counts = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            int val = Integer.parseInt(elements[i]);
            // Logic: A[i] - i = A[j] - j
            int diff = val - i; 
            counts.put(diff, counts.getOrDefault(diff, 0L) + 1);
        }
        
        long totalPairs = 0;
        
        // For every group of K elements that have the same (A[i] - i)
        // The number of ordered pairs (i, j) with i != j is K * (K - 1)
        for (long k : counts.values()) {
            if (k > 1) {
                totalPairs += k * (k - 1);
            }
        }
        
        System.out.println(totalPairs);
    }
}

