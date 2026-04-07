import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # First integer is the number of test cases T
    t = int(input_data[0])
    current_idx = 1
    
    for _ in range(t):
        # Read N and K
        n = int(input_data[current_idx])
        k = int(input_data[current_idx + 1])
        # Read string S
        s = input_data[current_idx + 2]
        current_idx += 3
        
        # Condition 1: Check if s[0] appears at least K times
        first_char = s[0]
        has_k_same = s.count(first_char) >= k
        
        # Condition 2: Check if there are at least K unique characters
        unique_chars_count = len(set(s))
        has_k_distinct = unique_chars_count >= k
        
        # If both conditions are met, print YES
        if has_k_same and has_k_distinct:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
