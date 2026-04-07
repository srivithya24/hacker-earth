import sys

def count_factors_of_2(n):
    """Counts how many times n can be divided by 2."""
    if n == 0:
        return 0  # Assuming positive integers; if 0 is possible, v2(0) is technically infinite.
    count = 0
    while n > 0 and n % 2 == 0:
        count += 1
        n //= 2
    return count

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T_cases = int(input_data[0])
    current_idx = 1
    
    results = []
    for _ in range(T_cases):
        N = int(input_data[current_idx])
        # The array size is 2 * N
        array_a = input_data[current_idx + 1 : current_idx + 1 + 2 * N]
        current_idx += 1 + 2 * N
        
        total_factors_of_2 = 0
        for x in array_a:
            total_factors_of_2 += count_factors_of_2(int(x))
            
        # Condition: Total factors of 2 must be at least N
        if total_factors_of_2 >= N:
            results.append("YES")
        else:
            results.append("NO")
            
    # Print all results separated by newline
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
