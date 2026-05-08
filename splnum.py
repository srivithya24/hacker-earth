MOD = 10**9 + 7

n = int(input())
arr = list(map(int, input().split()))

# primes up to 30
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# mask for every valid square-free number
masks = {}

for x in range(1, 31):

    temp = x
    mask = 0
    ok = True

    for i, p in enumerate(primes):

        cnt = 0

        while temp % p == 0:
            temp //= p
            cnt += 1

        # divisible by square
        if cnt > 1:
            ok = False
            break

        if cnt == 1:
            mask |= (1 << i)

    if ok:
        masks[x] = mask

# DP over bitmasks
dp = {0: 1}

for num in arr:

    if num not in masks:
        continue

    m = masks[num]

    new_dp = dp.copy()

    for old_mask, ways in dp.items():

        # no common prime factor
        if old_mask & m == 0:

            nm = old_mask | m

            new_dp[nm] = (new_dp.get(nm, 0) + ways) % MOD

    dp = new_dp

# remove empty subset
answer = (sum(dp.values()) - 1) % MOD

print(answer)
