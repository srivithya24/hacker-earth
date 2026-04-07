import sys

def solve():
    # Read all input values
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:]]
    
    if n == 0:
        return

    # 1. Identify contiguous blocks of identical elements
    # e.g., [0, 0, 1, 0, 1] has 4 blocks: [0,0], [1], [0], [1]
    block_info = []
    start = 0
    for i in range(1, n):
        if a[i] != a[i-1]:
            block_info.append((start + 1, i))
            start = i
    block_info.append((start + 1, n))
    
    c = len(block_info)
    
    # 2. Determine Minimum Total Score
    # If the array is all the same or K is large enough to isolate transitions
    all_same = all(x == a[0] for x in a)
    min_sum = 0 if (all_same or k >= c) else 1
    print("{0}".format(min_sum))
    
    # 3. Handle Partitioning
    if k < c:
        # Case where we can't separate all transitions
        # Greedy approach: first K-1 subarrays are size 1
        for i in range(1, k):
            print("{0} {1}".format(i, i))
        print("{0} {1}".format(k, n))
    else:
        # Case where we can achieve score 0
        # Split blocks into exactly K subarrays
        remaining_k = k
        for i in range(c):
            b_start, b_end = block_info[i]
            b_len = b_end - b_start + 1
            
            # Determine how many subarrays to pull from this pure block
            # We must leave at least 1 for each remaining block
            take = min(b_len, remaining_k - (c - i - 1))
            
            # Print (take-1) subarrays of length 1
            for j in range(take - 1):
                pos = b_start + j
                print("{0} {1}".format(pos, pos))
            
            # The last subarray of this block takes the remainder
            last_p_start = b_start + take - 1
            print("{0} {1}".format(last_p_start, b_end))
            
            remaining_k -= take

if __name__ == "__main__":
    solve()
