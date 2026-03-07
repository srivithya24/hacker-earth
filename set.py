import sys

def solve():
    # Use fast I/O to read N
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        n = int(input_data[0])
    except ValueError:
        return

    # Use a set to remove exact duplicates immediately
    unique_strings = list(set(input_data[1:n+1]))
    
    # Sort strings by length ascending
    # This helps because a longer string can't be a substring of a shorter one
    unique_strings.sort(key=len)
    
    ans_count = 0
    n_unique = len(unique_strings)
    
    for i in range(n_unique):
        is_minimal = True
        for j in range(n_unique):
            if i == j:
                continue
            
            # If any OTHER string 'j' is a substring of our current string 'i',
            # then string 'i' is automatically covered by picking 'j'.
            # We don't need to pick 'i'.
            if unique_strings[j] in unique_strings[i]:
                is_minimal = False
                break
        
        # If no other string is a substring of this one, we MUST pick it
        if is_minimal:
            ans_count += 1
            
    sys.stdout.write(str(ans_count) + '\n')

if __name__ == "__main__":
    solve()
