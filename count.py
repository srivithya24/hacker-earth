import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Map to integers
    a = map(int, input_data[1:])
    
    MOD = 1000000007
    
    # Linear Basis array (assuming numbers fit in 64 bits)
    basis = [0] * 64
    rank = 0
    
    for x in a:
        for i in range(63, -1, -1):
            # If the i-th bit is not set, skip
            if not (x >> i) & 1:
                continue
            
            # If no basis element exists for this bit, add it
            if not basis[i]:
                basis[i] = x
                rank += 1
                break
            
            # Otherwise, XOR and continue to lower bits
            x ^= basis[i]
            
    # The number of subsets where XOR sum is 0 is 2^(N - rank)
    # pow(base, exp, mod) handles the large exponent and modulo efficiently
    result = pow(2, n - rank, MOD)
    
    sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    solve()
