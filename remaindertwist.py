def count_pairs(n, y):
    count = 0

    # If y = 0, all pairs are valid
    if y == 0:
        return n * n

    for b in range(y + 1, n + 1):

        full = n // b
        count += full * (b - y)

        rem = n % b

        if rem >= y:
            count += (rem - y + 1)

    return count


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = -1

    for y in range(n, -1, -1):

        if count_pairs(n, y) >= k:
            ans = y
            break

    print(ans)
